from uuid import uuid4

from jaswdr_rid import exceptions

RID_PREFFIX = "rid"
RID_SEP = ":"


class Resource:
    def __init__(
        self,
        partition: str,
        service: str,
        region: str,
        account_id: str,
        resource_type: str,
        resource_id: str = "",
    ):
        self.partition = partition
        self.service = service
        self.region = region
        self.account_id = account_id
        self.resource_type = resource_type
        if not resource_id:
            resource_id = str(uuid4())
        self.resource_id = resource_id

    def __str__(self):
        return RID_SEP.join(self.fields())

    def fields(self):
        return (
            RID_PREFFIX,
            self.partition,
            self.service,
            self.region,
            self.account_id,
            self.resource_type,
            str(self.resource_id),
        )

    @staticmethod
    def from_string(resource_id: str):
        if not resource_id.startswith(RID_PREFFIX):
            raise exceptions.NotResourceError(resource_id)

        if resource_id.count(RID_SEP) != 6:
            raise exceptions.InvalidResourceError(resource_id)

        split = resource_id.split(RID_SEP)
        return Resource(
            partition=split[1],
            service=split[2],
            region=split[3],
            account_id=split[4],
            resource_type=split[5],
            resource_id=split[6],
        )

    def __eq__(self, other):
        if not isinstance(other, Resource):
            return False

        return all(
            [
                self.partition == other.partition,
                self.service == other.service,
                self.region == other.region,
                self.account_id == other.account_id,
                self.resource_type == other.resource_type,
                self.resource_id == other.resource_id,
            ]
        )

    def in_partition(self, target_partition: str) -> bool:
        return self.partition == target_partition

    def is_service(self, target_service: str) -> bool:
        return self.service == target_service

    def in_region(self, target_region: str) -> bool:
        return self.region == target_region

    def belongs_to(self, target_account_id: str) -> bool:
        return self.account_id == target_account_id

    def is_resource_type(self, target_resource_type: str) -> bool:
        return self.resource_type == target_resource_type

    def has_id(self, target_id: str) -> bool:
        return self.resource_id == target_id
