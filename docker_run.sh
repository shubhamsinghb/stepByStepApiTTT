docker build -t dockerttt .

docker run \
  -v $(pwd)/config:/qaAutomation/config \
  -e ENV=staging \
  -e SLACK_AUTH_TOKEN_QA=xoxb-4423125369925-4428559872756-IClVVxEpQusBDtxFiHbvogmA \
  dockerttt pytest \
  --color=yes