# Welcome

## Description
The flag is b64decode("d2UlN0I1ODRjNGNiMC1jYjU4LTQ1YWItOTNhNC0yOWY1YmRhYzlmMjJAaGVsbG9faGFja2VycyU3RSU3RA==")

# Solution
1. Decoding from base64 yields `we%7B584c4cb0-cb58-45ab-93a4-29f5bdac9f22@hello_hackers%7E%7D`
2. We notice `%7B`, `%7E`, `%7D`, suggesting URL encoding
3. Decoding from URL encoding gives the flag

> we{584c4cb0-cb58-45ab-93a4-29f5bdac9f22@hello_hackers~}