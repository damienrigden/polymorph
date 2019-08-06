# polymorph
Repository for the polymorph crypto problem

`polymorph()` and `depoly()` are encryption / decryption funtions.

The code in Polymorph.py depicts a terminal session interacting with these functions.

Figure out how to decode the encrypted question, and send me an encrypted answer such that `depoly()` will decrypt it.

Submit pull requests of Requests.py for any messages you want encoded, and any messages you want decoded (other than the solution), and I will add the results into the file. I started the file by encrypting all of the requests from **awakening** at the time of this commit.

Submit pull requests to README.md for any questions or clarification.

I learned a lot from making **awakening** and I think came up with some creative ways to make this more secure. So I feel this is a more challenging problem.

I have added a testdata folder with checks of the `polymorph()` and `depoly()` functions, and large random generated lists of encryptions.

The `polymorph()` function is not deterministic, however there is a large but finite number of possible combinations for each exact string.

Enjoy!
