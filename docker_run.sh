docker build -t dockerttt .

docker run \
  -v $(pwd)/config:/qaAutomation/config \
  -e ENV=staging \
  dockerttt pytest \
  --color=yes