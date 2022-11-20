docker build -t mydocker .

set -x


docker run \
  -v $(pwd)/config:/qaAutomation/config \
  -e ENV=staging \
  mydocker pytest \
  --color=yes