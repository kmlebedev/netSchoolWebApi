codegen_go:
	docker run --rm -v ${PWD}:/local swaggerapi/swagger-codegen-cli generate \
		-i /local/swagger/swagger.yaml \
		-l go \
		-o /local/go