lint:
	flake8 src

test: lint
	sh prepare.sh
	coverage run -m unittest discover buf
	coverage report

clean:
	rm -rf buf/
	rm .coverage