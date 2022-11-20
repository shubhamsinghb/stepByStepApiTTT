docker build -t mydocker .

set -x


docker run \
  -v $(pwd)/config:/qaAutomation/config \
  -e ENV=${ENVIRONMENT} \
  mydocker pytest \
  --color=yes