docker build -t dockerttt .

docker run \
  -v $(pwd)/config:/qaAutomation/config \
  -e ENV=staging \
  -e SLACK_AUTH_TOKEN_QA=write_your_slack_token_here \
  dockerttt pytest \
  --color=yes
