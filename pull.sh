curl -H "Authorization: token $github_token" -X POST -d "{ \"title\":\"${TRAVIS_BRANCH}\",\"head\":\"${TRAVIS_BRANCH}\",\"base\":\"master\", \"body\": \"${TRAVIS_COMMIT_MESSAGE}\" }" "https://api.github.com/repos/${TRAVIS_REPO_SLUG}/pulls"

