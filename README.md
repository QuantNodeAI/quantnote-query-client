# QuantNote Query Api

[![Python](https://img.shields.io/badge/Python-14354C?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Apache_2.0-yellow.svg)](LICENSE)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/company/quantnote/about/)
[![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=flat&logo=telegram&logoColor=white)](https://t.me/quantnote)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=flat&logo=github&logoColor=white)](https://github.com/QuantNote)

## Table of Content

<details>
<summary>Click to expand!</summary>

- [Description](#description)
- [Usage](#usage)
- [License](#license)

</details>

## Description

_QuantNote_ provides **Query API for on-chain data** for numerous blockchains, news & social media data, and
comprehensive quant models.
All under one roof.

_QuantNote_ is a data provider that offers on-chain data from EVM compatible blockchains, news & social media data and
models.
With our analytical tools, you can find **best entry points** for your trades, **analyze price data** or **create
machine learning models** for cryptocurrencies with ease.

Check out the [website](https://quantnote.com/) for more information!

## Usage

Getting data is as simple as calling one method with your SQL query!

You need to obtain your *auth_token* first, so you can request our API. Then your can easily create `client` object with
*auth_token* provided and start using API.

So you build your query for desired data and then easily call one `client` method, which return `pandas.DataFrame`
object.

See [`main_example.py`](main_example.py) file for primitive example usage of the client.

For more examples see [examples](examples) directory, which contains a collection of advanced examples written in the
Jupyter Notebook.

## License

[![License](https://img.shields.io/badge/License-Apache_2.0-yellow.svg)](LICENSE)

This package is licensed under the [Apache 2.0](LICENSE), so it is open source.

-------------------------------------------

[![](https://img.shields.io/badge/back%20to%20top-%E2%86%A9-blue)](#quantnote-query-api)
