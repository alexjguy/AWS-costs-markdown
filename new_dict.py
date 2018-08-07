#the datacenter that we need output for
location_filter = ["US East (Ohio)"]

#the list of OS that we need
operatingSystem_filter = ["RHEL", "Windows", "SUSE"]

#the list of instance types that we need output for
instanceType_filter = [
    "t2.nano",
    "t2.micro",
    "t2.small",
    "t2.medium",
    "t2.large",
    "t2.xlarge",
    "t2.2xlarge",

    "m5d.large",
    "m5d.xlarge",
    "m5d.2xlarge",
    "m5d.4xlarge",
    "m5d.12xlarge",
    "m5d.24xlarge",
  
    "m5.large",
    "m5.xlarge",
    "m5.2xlarge",
    "m5.4xlarge",
    "m5.12xlarge",
    "m5.24xlarge",  

    "m4.large",
    "m4.xlarge",
    "m4.2xlarge",
    "m4.4xlarge",
    "m4.10xlarge",
    "m4.16xlarge",

    "c5d.large",
    "c5d.xlarge",
    "c5d.2xlarge",
    "c5d.4xlarge",
    "c5d.9xlarge",
    "c5d.18xlarge",

    "c5.large",
    "c5.xlarge",
    "c5.2xlarge",
    "c5.4xlarge",
    "c5.9xlarge",
    "c5.18xlarge",

    "c4.large",
    "c4.xlarge",
    "c4.2xlarge",
    "c4.4xlarge",
    "c4.8xlarge",

    "g3.4xlarge",
    "g3.8xlarge",
    "g3.16xlarge",

    "p2.xlarge",
    "p2.8xlarge",
    "p2.16xlarge",

    "p3.2xlarge",
    "p3.8xlarge",
    "p3.16xlarge",

    "r4.large",
    "r4.xlarge",
    "r4.2xlarge",
    "r4.4xlarge",
    "r4.8xlarge",
    "r4.16xlarge",

    "x1.16xlarge"
    "x1.32xlarge"

    "d2.xlarge",
    "d2.2xlarge",
    "d2.4xlarge",
    "d2.8xlarge",

    "i2.xlarge",
    "i2.2xlarge",
    "i2.4xlarge",
    "i2.8xlarge",

    "h1.2xlarge",
    "h1.4xlarge",
    "h1.8xlarge",
    "h1.16xlarge",

    "i3.large",
    "i3.xlarge",
    "i3.2xlarge",
    "i3.4xlarge",
    "i3.8xlarge",
    "i3.16xlarge",
    "i3.metal"
]
#{"transferType" : "IntraRegion","endpointType" : "IPsec","transferType" : "AWS Inbound","transferType" : "AWS Outbound",}
vpc_productArr=["AWS Outbound", "IntraRegion", "ElasticIP:Address", "ElasticIP:AdditionalAddress", "CreateVpnConnection", "VPCE:VpcEndpoint", "NatGateway", "VPN Per Hour"]
s3_productArr=["Standard Access", "Standard-Infrequent Access", "One Zone-Infrequent Access", "Amazon Glacier Requests"]
usageType_filter = ["USE2-VPN-Usage-Hours:ipsec.1", "USE2-DataTransfer-In-Bytes", "USE2-DataTransfer-Out-Bytes","USE2-DataTransfer-Regional-Bytes"]
productFamily_filter = ["Data Transfer", "VpcEndpoint", "Cloud Connectivity", "IP Address", "NAT Gateway", "Load Balancer-Network","Storage", "API Request","Compute Instance" ]

dict = {
  "services":{
    "AmazonCloudWatch" : {
      "url":"https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonCloudWatch/current/index.json",
      "file":"CloudWatch.json",
      "productFamilies": ["Data Payload","Storage Snapshot","Metric","Alarm","Dashboard", "API Request"]
  },
    "AmazonS3" :{
    "url":"https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/S3/current/index.json",
    "file": "S3.json",
    "productFamilies": []
  }
},
"regions": ["US East (Ohio)"]
}


def init_dict():
  global aws_costs
  aws_costs = {}
  aws_costs['Region']={}

  for location in dict['regions']:
    aws_costs['Region'][location] = {}
    for service,v in dict['services'].items():
      try:
        x = aws_costs['Region'][location]['services']
      except KeyError:
        aws_costs['Region'][location]['services'] = {}
      try:
        x = aws_costs['Region'][location]['services'][service]
      except KeyError:
        aws_costs['Region'][location]['services'][service] = {}

    # for productFamily in productFamily_filter:
    #   try:
    #     x = aws_costs['Region'][location]['Product Family']
    #   except KeyError:
    #     aws_costs['Region'][location]['Product Family'] = {}

    #   try:
    #     x = aws_costs['Region'][location]['Product Family'][productFamily]
    #   except KeyError:
    #     aws_costs['Region'][location]['Product Family'][productFamily] = {}

    #   if (productFamily not in ['Storage', 'API Request']):
    #     for vpc_product in vpc_productArr:
    #       aws_costs['Region'][location]['Product Family'][productFamily][vpc_product]={}

    #   if (productFamily == "Storage"):
    #     aws_costs['Region'][location]['Product Family'][productFamily]['Storage']={}

    #   if (productFamily == "API Request"):
    #     for s3_product in s3_productArr:
    #       aws_costs['Region'][location]['Product Family'][productFamily][s3_product]={}

    # for operatingSystem in operatingSystem_filter:
    #   try:
    #     x = aws_costs['Region'][location]['Product Family']['Compute Instance']['Operating Systems']
    #   except KeyError:
    #     aws_costs['Region'][location]['Product Family']['Compute Instance']['Operating Systems'] = {}

    #   try:
    #     x = aws_costs['Region'][location]['Product Family']['Compute Instance']['Operating Systems'][operatingSystem]
    #   except KeyError:
    #     aws_costs['Region'][location]['Product Family']['Compute Instance']['Operating Systems'][operatingSystem] = {}
    #   for instanceType in instanceType_filter:
    #     aws_costs['Region'][location]['Product Family']['Compute Instance']['Operating Systems'][operatingSystem][instanceType]={}

init_dict()
print(aws_costs)