from aws_cdk import core
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_iam as iam

from constructs import Construct


class Desafio192CfStack(core.Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = ec2.Vpc(
            self,
            "last_vpc",
            cidr="192.168.0.0/16",
            max_azs=2,
            enable_dns_hostnames=True,
            enable_dns_support=True,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="PublicSubnet",
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=24,
                ),
                ec2.SubnetConfiguration(
                    name="PrivateSubnet",
                    subnet_type=ec2.SubnetType.PRIVATE_ISOLATED,
                    cidr_mask=24,
                ),
            ],
        )

        sg_final = ec2.SecurityGroup(
            self,
            "last_sg",
            vpc=vpc,
            description="Last security group!",
            disable_inline_rules=True,
            allow_all_outbound=True,
        )

        sg_final.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(22),
            description="Allow SSH access from anywhere",
        )

        existing_role = iam.Role.from_role_arn(self, 'ExistingRole',
            role_arn='arn:aws:sts::381491990760:assumed-role/voclabs/user2945116=__caro_Abreu'
        )

        instance = ec2.Instance(
            self,
            "last_instance",
            instance_type=ec2.InstanceType("t3.micro"),
            machine_image=ec2.MachineImage.latest_amazon_linux(),
            vpc=vpc,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_ISOLATED),
            security_group=sg_final,
            role=existing_role,
        )
