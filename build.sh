docker build --tag rpm_builder .
docker run --cap-add=SYS_ADMIN --volume $PWD/cache:/var/cache/mock --volume $PWD:/spec_src rpm_builder $1
