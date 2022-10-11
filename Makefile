codegen_go:
	docker run --rm -v ${PWD}:/local swaggerapi/swagger-codegen-cli-v3 generate -i /local/swagger/swagger.yaml -l go -o /local/go

codegen:
	for lang in csharp go java kotlin-client php python ruby scala javascript; do \
  		docker run --rm -v ${PWD}:/local swaggerapi/swagger-codegen-cli-v3 generate -i /local/swagger/swagger.yaml -l $$lang -o /local/$$lang; \
	done