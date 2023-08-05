/*
  Copyright (C) 2020- The Blosc Development Team <blosc@blosc.org>
  http://blosc.org
  License: BSD (see LICENSE.txt)

  Creation date: 2020-09-25

  See LICENSE.txt for details about copyright and rights to use.
*/

#include <stdio.h>
#include "test_common.h"

#define CHUNKSIZE (200 * 1000)
#define NTHREADS (2)

/* Global vars */
int tests_run = 0;
int nchunks;
bool copy;


static char* test_schunk(void) {
  static int32_t data[CHUNKSIZE];
  static int32_t data_dest[CHUNKSIZE];
  int32_t isize = CHUNKSIZE * sizeof(int32_t);
  int64_t nbytes, cbytes;
  blosc2_cparams cparams = BLOSC2_CPARAMS_DEFAULTS;
  blosc2_dparams dparams = BLOSC2_DPARAMS_DEFAULTS;
  blosc2_schunk* schunk;

  /* Initialize the Blosc compressor */
  blosc_init();

  /* Create a super-chunk container */
  cparams.typesize = sizeof(int32_t);
  cparams.nthreads = NTHREADS;
  dparams.nthreads = NTHREADS;
  blosc2_storage storage = {.cparams=&cparams, .dparams=&dparams};
  schunk = blosc2_schunk_empty(nchunks, &storage);

  // Add a couple of metalayers
  blosc2_meta_add(schunk, "metalayer1", (uint8_t *) "my metalayer1", sizeof("my metalayer1"));
  blosc2_meta_add(schunk, "metalayer2", (uint8_t *) "my metalayer1", sizeof("my metalayer1"));

  bool needs_free;
  int32_t datasize = sizeof(int32_t) * CHUNKSIZE;
  int32_t chunksize = sizeof(int32_t) * CHUNKSIZE + BLOSC_MAX_OVERHEAD;

  // Feed it with data
  uint8_t *chunk;
  int csize;
  int nchunks_;

  for (int nchunk = 0; nchunk < nchunks; nchunk++) {
    for (int i = 0; i < CHUNKSIZE; i++) {
      data[i] = i + nchunk * CHUNKSIZE;
    }

    chunk = malloc(chunksize);
    csize = blosc2_compress_ctx(schunk->cctx, data, datasize, chunk, chunksize);
    mu_assert("ERROR: chunk cannot be compressed", csize >= 0);
    nchunks_ = blosc2_schunk_update_chunk(schunk, nchunk, chunk, copy);
    mu_assert("ERROR: bad append in schunk", nchunks_ == nchunks);

    chunk = malloc(chunksize);
    csize = blosc2_compress_ctx(schunk->cctx, data, datasize, chunk, chunksize);
    mu_assert("ERROR: chunk cannot be compressed", csize >= 0);
    nchunks_ = blosc2_schunk_update_chunk(schunk, nchunk, chunk, copy);

    mu_assert("ERROR: bad append in schunk", nchunks_ == nchunks);

    if (copy) {
      free(chunk);
    }
  }

  blosc2_meta_update(schunk, "metalayer2", (uint8_t *) "my metalayer2", sizeof("my metalayer2"));
  // Attach some user metadata into it
  blosc2_vlmeta_add(schunk, "vlmetalayer", (uint8_t *) "testing the vlmetalayers", 16, NULL);

  /* Gather some info */
  nbytes = schunk->nbytes;
  cbytes = schunk->cbytes;
  if (nchunks > 0) {
    mu_assert("ERROR: bad compression ratio in frame", nbytes > 10 * cbytes);
  }

  // Exercise the metadata retrieval machinery
  size_t nbytes_, cbytes_, blocksize;
  nbytes = 0;
  cbytes = 0;
  for (int nchunk = 0; nchunk < nchunks; nchunk++) {
    cbytes_ = blosc2_schunk_get_chunk(schunk, nchunk, &chunk, &needs_free);
    mu_assert("ERROR: chunk cannot be retrieved correctly.", cbytes_ >= 0);
    blosc_cbuffer_sizes(chunk, &nbytes_, &cbytes_, &blocksize);
    nbytes += nbytes_;
    cbytes += cbytes_;
    if (needs_free) {
      free(chunk);
    }
  }
  mu_assert("ERROR: nbytes is not correct", nbytes == schunk->nbytes);
  mu_assert("ERROR: cbytes is not correct", cbytes == schunk->cbytes);

  // Check that the chunks have been decompressed correctly
  for (int nchunk = 0; nchunk < nchunks; nchunk++) {
    cbytes = blosc2_schunk_decompress_chunk(schunk, nchunk, (void *) data_dest, isize);
    mu_assert("ERROR: chunk cannot be decompressed correctly.", cbytes >= 0);
    for (int i = 0; i < CHUNKSIZE; i++) {
      mu_assert("ERROR: bad roundtrip",data_dest[i] == i + nchunk * CHUNKSIZE);
    }
  }

  // metalayers
  uint8_t* content;
  uint32_t content_len;
  blosc2_meta_get(schunk, "metalayer1", &content, &content_len);
  mu_assert("ERROR: bad metalayer content", strncmp((char*)content, "my metalayer1", content_len) == 0);
  if (content != NULL) {
    free(content);
  }
  blosc2_meta_get(schunk, "metalayer2", &content, &content_len);
  mu_assert("ERROR: bad metalayer content", strncmp((char*)content, "my metalayer2", content_len) == 0);
  if (content != NULL) {
    free(content);
  }

  // Check the vlmetalayers
  uint8_t* content2;
  uint32_t content2_len;
  blosc2_vlmeta_get(schunk, "vlmetalayer", &content2, &content2_len);

  mu_assert("ERROR: bad vlmetalayers", strncmp((char*)content2, "testing the vlmetalayers", 16) == 0);
  mu_assert("ERROR: bad vlmetalayer_len", content2_len == 16);
  free(content2);

  /* Free resources */
  blosc2_schunk_free(schunk);
  /* Destroy the Blosc environment */
  blosc_destroy();

  return EXIT_SUCCESS;
}

static char *all_tests(void) {
  nchunks = 0;
  copy = true;
  mu_run_test(test_schunk);

  nchunks = 6;
  copy = true;
  mu_run_test(test_schunk);

  nchunks = 22;
  copy = false;
  mu_run_test(test_schunk);

  nchunks = 10;
  copy = true;
  mu_run_test(test_schunk);

  return EXIT_SUCCESS;
}


int main(void) {
  char *result;

  install_blosc_callback_test(); /* optionally install callback test */
  blosc_init();

  /* Run all the suite */
  result = all_tests();
  if (result != EXIT_SUCCESS) {
    printf(" (%s)\n", result);
  }
  else {
    printf(" ALL TESTS PASSED");
  }
  printf("\tTests run: %d\n", tests_run);

  blosc_destroy();

  return result != EXIT_SUCCESS;
}
