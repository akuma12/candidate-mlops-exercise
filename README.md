# Instructions
We've provided a VERY basic Python script to perform inference against the Hugging Face `bert-base-uncased` model. This model takes in a string with a `[MASK]` key. The model will respond with 
a list of JSON objects containing a probability score, a token, the token string (the value that will fill in `[MASK]`), and the original string with the `[MASK]` key replaced.

For example:

Input:
```
"Hello I'm a [MASK] model."
```

Output:
```
[
    {
        "score": 0.10731063783168793,
        "token": 4827,
        "token_str": "fashion",
        "sequence": "hello i'm a fashion model."
    },
    {
        "score": 0.08774515986442566,
        "token": 2535,
        "token_str": "role",
        "sequence": "hello i'm a role model."
    },
    {
        "score": 0.05338398739695549,
        "token": 2047,
        "token_str": "new",
        "sequence": "hello i'm a new model."
    },
    {
        "score": 0.04667206481099129,
        "token": 3565,
        "token_str": "super",
        "sequence": "hello i'm a super model."
    },
    {
        "score": 0.027095932513475418,
        "token": 2986,
        "token_str": "fine",
        "sequence": "hello i'm a fine model."
    }
]
```

We would like you to create a REST API service with 2 endpoints:
* `/inference`: This endpoint should accept the string to replace in a JSON object by POST, and respond with the JSON provided by the model.
* `/healthcheck`: This endpoint should return an HTTP 200.

It's up to you which REST framework you prefer to use, be it Flask, FastAPI, or Django.

Please timebox your work to 2-4 hours. If you finish up the API quickly, feel free to try to hit some of the bonus points listed below.

# To perform this excercise
1. Fork this repo.
2. Commit your changes to your fork.
3. Submit a link to your fork, along with an explanation of your choices (such as REST framework, or anything else you want to point out). This can be in a README in your repo, or a few paragraphs in your response email.

# What we would like to see
* A working REST API.
* Any additional Python requirements added to `requirements.txt`.
* API documentation! At the very least a README file with the expected input as a cURL call, and sample JSON output.
  * Bonus points if you add an API documentation endpoint using something like OpenAPI.
* Please use good Python formatting, adhering to PEP8 standards. Pylint should return a 9.0 quality score or higher.
* Tell us what else you would do to make this model ready for production use.

# Bonus Points
* Dockerize the application.
* Create a pipeline to automatically build and deploy the application to a server.
* Add a unit test to validate inference output.
* Implement a different model.

# How will you be evaluated
We're not looking for perfection; we really want to see how you tackle a problem, so please document your process.

If you had to Google 90% of it to get it to work, THAT'S OK! It's not always about knowing the right answer,
it's about knowing how to get the right answer. If you found solutions on the Internet, please cite them in your explanation.
