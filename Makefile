include .env
export

docker_build_local:
	docker build -t ${DOCKER_IMAGE_NAME}:dev .

docker_run:
	docker run --env-file .env -p ${PORT}:${PORT} ${DOCKER_IMAGE_NAME}:dev

IMAGE_URI = ${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT}/${ARTIFACTSREPO}/${DOCKER_IMAGE_NAME}:prod

docker_build_gcp:
	docker build --platform linux/amd64 -t ${IMAGE_URI} .

docker_push:
	docker push ${IMAGE_URI}

docker_deploy:
	gcloud run deploy ${DOCKER_IMAGE_NAME} \
		--image ${IMAGE_URI} \
		--region ${GCP_REGION} \
		--allow-unauthenticated
