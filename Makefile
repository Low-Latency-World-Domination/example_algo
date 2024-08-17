build:
	python -m grpc_tools.protoc -Isp_proto/ --python_out=. --grpc_python_out=. --pyi_out=. ./sp_proto/*.proto
	# mypy -m ./trader_pb2_grpc
