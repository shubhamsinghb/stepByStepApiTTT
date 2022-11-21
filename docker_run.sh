docker build -t mydocker .

docker run \
  -v $(pwd)/config:/qaAutomation/config \
  -e ENV=${ENVIRONMENT} \
  mydocker pytest \
  --color=yes