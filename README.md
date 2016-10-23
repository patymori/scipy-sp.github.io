Site Observatório do SciPy-SP
====================


Instalando e Rodando
--------------------

- Assumindo que você já fez um _fork_ do projeto, faça o clone do seu repositório:

		$ git clone git@github.com:<seu-login>/scipy-sp.github.io.git

- Crie um virtualenv (pode chamar de `venv`) com python3. Se ocorrer algum erro ao criar um virtualenv, [leia isso](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

		$ virtualenv venv -p python3

(Atenção: se você estiver usando um **MacOS X** para desenvolver, você provavelmente precisará exportar algumas variáveis locale do Python. Siga esse link: [Fix unknown locale](http://patrick.arminio.info/fix-valueerror-unknown-locale-utf8/))

- Ative seu virtualenv e instale os pacotes necessários para rodar o projeto:

		$ source bin/venv/activate
		$ pip install -r requirements.txt

- Rode o projeto

		$ make clean html serve

Abra o navegador em [localhost:8000](http://localhost:8000) para ver o conteúdo gerado.

Contribuindo
------------

Para contribuir com o projeto veja o guia de [Contribuição](CONTRIBUTING.md).

Fazendo o deploy
----------------

Para fazer o deploy, você precisa ter permissão de escrita no repositório oficial, e fazer:

		$ make github


Links Úteis
-----------

* Documentação Pelican - http://docs.getpelican.com/en/3.6.3/
* Virtualenv - http://docs.python-guide.org/en/latest/dev/virtualenvs/
* Pyenv - https://github.com/yyuu/pyenv
