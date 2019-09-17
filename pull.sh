 curl -H \
  Authorization: token  32fc1954d3604f60c1e1e65a7d15ea61bb18f50e\
  -X POST -d\
  "{ \"title\":\"title\",\"head\":\"${TRAVIS_HEAD}\",\"base\":\"master\", \"body\": \"Hello world\", }"\
  "https://api.github.com/repos/${TRAVIS_REPO_SLUG}/pulls"

