AWS Backend
===========

Using Coiled's AWS account
--------------------------

By default your computations run inside Coiled's AWS account. This makes it easy
for you to get started quickly, without needing to set up any additional
infrastructure.

.. figure:: images/backend-coiled-aws-vm.png


Using your own AWS account
--------------------------

You can have Coiled run computations in your own AWS account. This allows you to
take advantage of any account or security configurations (such as startup
credits or custom data access controls) that you already have in place. When
configuring AWS as a backend in the Account page of your Coiled account, you can
choose to run Coiled using an ECS-based backend or a VM-based backend.

When you chose to run Coiled in your own AWS account, Coiled will create the
necessary networking resources. You should ensure that you have enough Elastic
IP addresses for each availability zone in your chosen region. Otherwise Coiled
will not be able to create the needed networking resources.

For the ECS backend, Coiled will create one Elastic IP address per availability
zone. For the VM backend, Coiled will create one Elastic IP address. Please refer
to the `AWS regions page <https://aws.amazon.com/about-aws/global-infrastructure/regions_az/>`_
to determine how many availability zones are available in your desired region,
which is also the number of Elastic IP addresses that Coiled will create.

.. attention::

  The necessary resources will be created when you launch your first cluster. This
  initial work can take up to 20 minutes. Once all the resources are created, the
  following clusters you launch will be much faster - they will usually be created
  under 5 minutes.

.. figure:: images/backend-external-aws-vm.png

To do this,
`create an access key ID and secret access key <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>`_
and add them to the "Cloud Backend Options" section of the Account page of your
Coiled account.

From now on, clusters you create with Coiled will be launched in your AWS
account.

.. note::

    The AWS credentials you supply must be long-lived (not temporary) tokens,
    and have sufficient permissions to allow Coiled to set up management
    infrastructure and create & launch compute resources from within your AWS
    account.

    Also, note that if you have not used AWS Elastic Container Service in this
    account before, you may need to
    `create the necessary service-linked IAM role <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using-service-linked-roles.html>`_
    -- we cannot yet create it automatically.

The below JSON template lists all the above permissions and can be used to
`create the required IAM policy directly <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html#access_policies_create-json-editor>`_.

.. dropdown:: IAM policy template
  :title: bg-white

  .. code-block:: json

        {
          "Statement": [
            {
              "Sid": "Setup",
              "Effect": "Allow",
              "Resource": "*",
              "Action": [
                "ec2:AllocateAddress",
                "ec2:AssociateRouteTable",
                "ec2:AttachInternetGateway",
                "ec2:CreateInternetGateway",
                "ec2:CreateNatGateway",
                "ec2:CreateRoute",
                "ec2:CreateRouteTable",
                "ec2:CreateSubnet",
                "ec2:CreateVpc",
                "ec2:CreateVpcPeeringConnection",
                "ec2:DeleteInternetGateway",
                "ec2:DeleteNatGateway",
                "ec2:DeleteRoute",
                "ec2:DeleteRouteTable",
                "ec2:DeleteSubnet",
                "ec2:DeleteVpc",
                "ec2:DeleteVpcPeeringConnection",
                "ec2:DescribeAddresses",
                "ec2:DescribeInternetGateways",
                "ec2:DetachInternetGateway",
                "ec2:DisassociateAddress",
                "ec2:GetConsoleOutput",
                "ec2:ModifySubnetAttribute",
                "ec2:ModifyVpcAttribute",
                "ec2:ReleaseAddress",
                "ecs:CreateCluster",
                "iam:AttachRolePolicy",
                "iam:CreateRole",
                "iam:CreatePolicy",
                "iam:DeleteRole",
                "iam:ListPolicies",
                "iam:TagRole",
                "secretsmanager:CreateSecret",
                "secretsmanager:DeleteSecret",
                "secretsmanager:DescribeSecret",
                "secretsmanager:GetSecretValue",
                "secretsmanager:TagResource"
              ]
            },
            {
              "Sid": "Ongoing",
              "Effect": "Allow",
              "Resource": "*",
              "Action": [
                "ec2:AuthorizeSecurityGroupIngress",
                "ec2:CreateImage",
                "ec2:CreateSecurityGroup",
                "ec2:CreateTags",
                "ec2:DeleteSecurityGroup",
                "ec2:DescribeAvailabilityZones",
                "ec2:DescribeConversionTasks",
                "ec2:DescribeImages",
                "ec2:DescribeInstanceTypes",
                "ec2:DescribeInstances",
                "ec2:DescribeKeyPairs",
                "ec2:DescribeNatGateways",
                "ec2:DescribeNetworkInterfaces",
                "ec2:DescribeRegions",
                "ec2:DescribeRouteTables",
                "ec2:DescribeSecurityGroups",
                "ec2:DescribeSubnets",
                "ec2:DescribeVpcPeeringConnections",
                "ec2:DescribeVpcs",
                "ec2:ImportKeyPair",
                "ec2:RunInstances",
                "ec2:TerminateInstances",
                "ecr:BatchCheckLayerAvailability",
                "ecr:BatchGetImage",
                "ecr:CompleteLayerUpload",
                "ecr:CreateRepository",
                "ecr:DescribeImages",
                "ecr:DescribeRepositories",
                "ecr:GetAuthorizationToken",
                "ecr:GetDownloadUrlForLayer",
                "ecr:GetRepositoryPolicy",
                "ecr:InitiateLayerUpload",
                "ecr:ListImages",
                "ecr:PutImage",
                "ecr:UploadLayerPart",
                "ecs:DescribeClusters",
                "ec2:DescribeInstanceTypeOfferings",
                "ecs:DescribeTaskDefinition",
                "ecs:DescribeTasks",
                "ecs:ListClusters",
                "ecs:ListTaskDefinitions",
                "ecs:ListTasks",
                "ecs:RegisterTaskDefinition",
                "ecs:RunTask",
                "ecs:StopTask",
                "iam:CreatePolicy",
                "iam:CreateServiceLinkedRole",
                "iam:GetRole",
                "iam:ListPolicies",
                "iam:PassRole",
                "iam:TagRole",
                "logs:CreateLogGroup",
                "logs:GetLogEvents",
                "logs:PutRetentionPolicy",
                "secretsmanager:CreateSecret",
                "secretsmanager:DeleteSecret",
                "secretsmanager:DescribeSecret",
                "secretsmanager:GetSecretValue",
                "secretsmanager:TagResource",
                "sts:GetCallerIdentity"
              ]
            }
          ],
          "Version": "2012-10-17"
        }

.. seealso::

  You might be interested in reading the knowledge base tutorial
  on :doc:`How to limit Coiled's access to your AWS resources <tutorials/aws_permissions>`.


AWS resources
-------------

When you create a Dask cluster with Coiled using the VM backend on your own AWS
account, Coiled will provision the following resources on your AWS account:


.. figure:: images/backend-coiled-aws-architecture.png
   :width: 90%

   AWS resources for a Dask cluster with 4 workers

If you create additional Dask clusters with Coiled, then another scheduler VM
and additional worker VMs will be provisioned within the same public and private
subnets, respectively. Coiled will also reuse the existing VPC and other
existing network resources.

.. seealso::

  If you encounter any issues when setting up resources, you can use the method
  :meth:`coiled.get_notifications` to have more visibility into this process.
  You might also be interested in reading our
  :doc:`Troubleshooting guide <troubleshooting/visibility_resource_creation>`.

Backend options
---------------

There are several AWS-specific options you can specify (listed below) to
customize Coiled's behavior. Additionally, the next section contains an example
of how to configure these options in practice.



.. list-table::
   :widths: 25 50 25
   :header-rows: 1

   * - Name
     - Description
     - Default
   * - ``region``
     - AWS region to create resources in
     - ``us-east-2``
   * - ``spot``
     - Whether or not to use spot instances for cluster workers
     - ``True``

The currently supported AWS regions are:

* ``us-east-1``
* ``us-east-2``
* ``us-west-1``
* ``us-west-2``
* ``eu-central-1``
* ``eu-west-2``

.. note::

  Coiled will choose the ``us-east-2`` region by default if you don't
  wish to use this region, you should provide a different region.

.. _backend_options_example:

Example
^^^^^^^

You can specify backend options directly in Python:

.. code-block::

    import coiled

    cluster = coiled.Cluster(backend_options={"region": "us-west-1"})

Or save them to your :ref:`Coiled configuration file <configuration>`:

.. code-block:: yaml

    # ~/.config/dask/coiled.yaml

    coiled:
      backend-options:
        region: us-west-1

to have them used as the default value for the ``backend_options=`` keyword:

.. code-block::

    import coiled

    cluster = coiled.Cluster()


GPU support
-----------

This backend allows you to run computations with GPU-enabled machines if your
account has access to GPUs. See the :doc:`GPU best practices <gpu>`
documentation for more information on using GPUs with this backend.

Workers currently have access to a single GPU, if you try to create a cluster
with more than one GPU, the cluster will not start, and an error will be
returned to you.
