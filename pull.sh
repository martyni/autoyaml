curl -H \
  "Authorization: token  afa7e54e1999c6f0a51ced7a6831113b3987a34a"\
  -X POST -d\
  "{ \"title\":\"${TRAVIS_BRNACH}\",\"head\":\"${TRAVIS_BRANCH}\",\"base\":\"master\", \"body\": \"${TRAVIS_COMMIT_MESSAGE}\", }"\
  "https://api.github.com/repos/${TRAVIS_REPO_SLUG}/pulls"
