import json
import requests


ec2_url = 'https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonEC2/current/index.json'
ec2_filename = 'ComputeInstance.json'

#Read JSON data into the datastore variable
if ec2_filename:
    try:
      with open(ec2_filename, 'r') as f:
        ec2_data = json.load(f)
    except:
      resp = requests.get(url=vpc_url)
      vpc_data = json.loads(resp.text)
else:
    resp = requests.get(url=ec2_ec2)
    ec2_data = json.loads(resp.text)

ec2_products = ec2_data['products']

vpc_url = 'https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonVPC/current/index.json'
vpc_filename = 'VPC.json'

#Read JSON data into the datastore variable
if vpc_filename:
    try:
      with open(vpc_filename, 'r') as f:
        vpc_data = json.load(f)
    except:
      resp = requests.get(url=vpc_url)
      vpc_data = json.loads(resp.text)
else:
    resp = requests.get(url=vpc_url)
    vpc_data = json.loads(resp.text)

vpc_products = vpc_data['products']
location_filter = ["US East (Ohio)"]
operatingSystem_filter = ["RHEL", "Windows", "SUSE"]
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
usageType_filter = ["USE2-VPN-Usage-Hours:ipsec.1", "USE2-DataTransfer-In-Bytes", "USE2-DataTransfer-Out-Bytes","USE2-DataTransfer-Regional-Bytes"]
productFamily_filter = ["Data Transfer", "VpcEndpoint", "Cloud Connectivity", "IP Address", "NAT Gateway", "Load Balancer-Network","Compute Instance"]



def init_dict():
  global aws_costs
  aws_costs = {}
  aws_costs['Region']={}

  for location in location_filter:
    aws_costs['Region'][location] = {}
    for productFamily in productFamily_filter:
      try:
        x = aws_costs['Region'][location]['Product Family']
      except KeyError:
        aws_costs['Region'][location]['Product Family'] = {}

      try:
        x = aws_costs['Region'][location]['Product Family'][productFamily]
      except KeyError:
        aws_costs['Region'][location]['Product Family'][productFamily] = {}
      for vpc_product in vpc_productArr:
        aws_costs['Region'][location]['Product Family'][productFamily][vpc_product]={}
      
    for operatingSystem in operatingSystem_filter:
      try:
        x = aws_costs['Region'][location]['Product Family']['Compute Instance']['Operating Systems']
      except KeyError:
        aws_costs['Region'][location]['Product Family']['Compute Instance']['Operating Systems'] = {}

      try:
        x = aws_costs['Region'][location]['Product Family']['Compute Instance']['Operating Systems'][operatingSystem]
      except KeyError:
        aws_costs['Region'][location]['Product Family']['Compute Instance']['Operating Systems'][operatingSystem] = {}
      for instanceType in instanceType_filter:
        aws_costs['Region'][location]['Product Family']['Compute Instance']['Operating Systems'][operatingSystem][instanceType]={}

####
hourlyTermCode = 'JRTCKXETXF'
hourlyRateCode = '6YS6EN2CT7'
upfrontFeeCode = '2TG2D8R56U'
### 1YR Standard
RI1YRNoUpfrontStdTermCode = '4NA7Y494T4'
RI1YRPartialUpfrontStdTermCode = 'HU7G6KETJZ'
RI1YRAllUpfrontStdTermCode = '6QCMYABX3D'
### 1 Year Convertible
RI1YRNoUpfrontConvTermCode = '7NE97W5U4E'
RI1YRPartialUpfrontConvTermCode = 'CUZHX8X6JH'
RI1YRAllUpfrontConvTermCode = 'VJWZNREJX2'
### 3 Year Standard
RI3YRNoUpfrontStdTermCode = 'BPH4J8HBKS'
RI3YRPartialUpfrontStdTermCode = '38NPMPTW36'
RI3YRAllUpfrontStdTermCode = 'NQ3QZPMQV9'
### 3 Year Convertible
RI3YRNoUpfrontConvTermCode = 'Z2E3P23VKM'
RI3YRPartialUpfrontConvTermCode = 'R5XV2EPZQZ'
RI3YRAllUpfrontConvTermCode = 'MZU6U2429S'
####



def return_aws_network_costs(vpc_products,ec2_products):
  for sku, product in ec2_products.items():

    #Data Transfer OUT From Amazon EC2 To Internet
    ##Up to 1 GB / Month 8EEUB22XNJ
    if (product['productFamily'] == "Data Transfer"):
      if (product['attributes']['transferType'] == "AWS Outbound" and
          product['attributes']['fromLocation'] in location_filter and
          product['attributes']['toLocation'] == "External"):
            aws_costs['Region'][product['attributes']['fromLocation']]['Product Family'][product['productFamily']][product['attributes']['transferType']]['Outgoing traffic cost per GB up to 1 GB / Month'] = \
            str(float(ec2_data['terms']['OnDemand'][sku][sku + '.' + hourlyTermCode]['priceDimensions'][sku + '.' + hourlyTermCode + '.8EEUB22XNJ']['pricePerUnit']['USD']))
    
      ##Next 9.999 TB / Month WVV8R9FH29
      if (product['attributes']['transferType'] == "AWS Outbound" and
          product['attributes']['fromLocation'] in location_filter and
          product['attributes']['toLocation'] == "External"):
            aws_costs['Region'][product['attributes']['fromLocation']]['Product Family'][product['productFamily']][product['attributes']['transferType']]['Outgoing traffic cost per GB up to 10 GB / Month'] = \
            str(float(ec2_data['terms']['OnDemand'][sku][sku + '.' + hourlyTermCode]['priceDimensions'][sku + '.' + hourlyTermCode + '.WVV8R9FH29']['pricePerUnit']['USD']))

      ##Next 40 TB / Month VF6T3GAUKQ
      if (product['attributes']['transferType'] == "AWS Outbound" and
          product['attributes']['fromLocation'] in location_filter and
          product['attributes']['toLocation'] == "External"):
            aws_costs['Region'][product['attributes']['fromLocation']]['Product Family'][product['productFamily']][product['attributes']['transferType']]['Outgoing traffic cost per GB up to 40 TB / Month'] = \
            str(float(ec2_data['terms']['OnDemand'][sku][sku + '.' + hourlyTermCode]['priceDimensions'][sku + '.' + hourlyTermCode + '.VF6T3GAUKQ']['pricePerUnit']['USD']))

      ##Next 100 TB / Month N9EW5UVVPA
      if (product['attributes']['transferType'] == "AWS Outbound" and
          product['attributes']['fromLocation'] in location_filter and
          product['attributes']['toLocation'] == "External"):
            aws_costs['Region'][product['attributes']['fromLocation']]['Product Family'][product['productFamily']][product['attributes']['transferType']]['Outgoing traffic cost per GB up to 100 TB / Month'] = \
            str(float(ec2_data['terms']['OnDemand'][sku][sku + '.' + hourlyTermCode]['priceDimensions'][sku + '.' + hourlyTermCode + '.N9EW5UVVPA']['pricePerUnit']['USD']))

      ##Greater than 150 TB / Month GPHXDESFBB
      if (product['attributes']['transferType'] == "AWS Outbound" and
          product['attributes']['fromLocation'] in location_filter and
          product['attributes']['toLocation'] == "External"):
            aws_costs['Region'][product['attributes']['fromLocation']]['Product Family'][product['productFamily']][product['attributes']['transferType']]['Outgoing traffic cost per GB grater than 150 TB / Month'] = \
            str(float(ec2_data['terms']['OnDemand'][sku][sku + '.' + hourlyTermCode]['priceDimensions'][sku + '.' + hourlyTermCode + '.GPHXDESFBB']['pricePerUnit']['USD']))

      #All data transfer in and out within the region	
      if (product['attributes']['transferType'] == "IntraRegion" and
          product['attributes']['fromLocation'] in location_filter and
          product['attributes']['toLocation'] in location_filter):
            aws_costs['Region'][product['attributes']['fromLocation']]['Product Family'][product['productFamily']][product['attributes']['transferType']]['All data transfer in and out within the region per GB'] = \
            str(float(ec2_data['terms']['OnDemand'][sku][sku + '.' + hourlyTermCode]['priceDimensions'][sku + '.' + hourlyTermCode + '.' + hourlyRateCode]['pricePerUnit']['USD']))

    if (product['productFamily'] == "IP Address"):

      #Elastic IP address
      if (product['attributes']['group'] == "ElasticIP:Address" and
          product['attributes']['location'] in location_filter):
            aws_costs['Region'][product['attributes']['location']]['Product Family'][product['productFamily']][product['attributes']['group']]['Elastic IP address not attached to a running instance for the first hour'] = \
            str(float(ec2_data['terms']['OnDemand'][sku][sku + '.' + hourlyTermCode]['priceDimensions'][sku + '.' + hourlyTermCode + '.8EEUB22XNJ']['pricePerUnit']['USD']))
            aws_costs['Region'][product['attributes']['location']]['Product Family'][product['productFamily']][product['attributes']['group']]['Elastic IP address not attached to a running instance per hour (prorated)'] = \
            str(float(ec2_data['terms']['OnDemand'][sku][sku + '.' + hourlyTermCode]['priceDimensions'][sku + '.' + hourlyTermCode + '.JTU8TKNAMW']['pricePerUnit']['USD']))

      #Additional Elastic IP address    
      if (product['attributes']['group'] == "ElasticIP:AdditionalAddress" and
          product['attributes']['location'] in location_filter):
            aws_costs['Region'][product['attributes']['location']]['Product Family'][product['productFamily']][product['attributes']['group']]['Additional Elastic IP address attached to a running instance per hour (prorated)'] = \
            str(float(ec2_data['terms']['OnDemand'][sku][sku + '.' + hourlyTermCode]['priceDimensions'][sku + '.' + hourlyTermCode + '.' + hourlyRateCode]['pricePerUnit']['USD']))

    #NAT Gateway
    if (product['productFamily'] == "NAT Gateway" and
        product['attributes']['location'] in location_filter and
        product['attributes']['operation'] == "NatGateway"):
          if (product['attributes']['groupDescription'] ==  "Hourly charge for NAT Gateways"):
            aws_costs['Region'][product['attributes']['location']]['Product Family'][product['productFamily']][product['attributes']['operation']]['NAT Gateway per hour'] = \
            str(float(ec2_data['terms']['OnDemand'][sku][sku + '.' + hourlyTermCode]['priceDimensions'][sku + '.' + hourlyTermCode + '.' + hourlyRateCode]['pricePerUnit']['USD']))
          if (product['attributes']['groupDescription'] ==  "Charge for per GB data processed by NatGateways"):
            aws_costs['Region'][product['attributes']['location']]['Product Family'][product['productFamily']][product['attributes']['operation']]['Nat Gateway per GB'] = \
            str(float(ec2_data['terms']['OnDemand'][sku][sku + '.' + hourlyTermCode]['priceDimensions'][sku + '.' + hourlyTermCode + '.' + hourlyRateCode]['pricePerUnit']['USD']))

  for sku, product in vpc_products.items():

    #VPN Connection
    if (product['attributes']['operation'] == "CreateVpnConnection" and 
        product['attributes']['location'] in location_filter):
          if (product['productFamily'] == "Cloud Connectivity"):
            aws_costs['Region'][product['attributes']['location']]['Product Family']['Cloud Connectivity'][product['attributes']['operation']]['VPN Connection per hour'] = \
            str(float(vpc_data['terms']['OnDemand'][sku][sku + '.' + hourlyTermCode]['priceDimensions'][sku + '.' + hourlyTermCode + '.' + hourlyRateCode]['pricePerUnit']['USD']))

    #VPC Endpoint
    if (product['attributes']['operation'] == "VpcEndpoint" and 
        product['attributes']['location'] in location_filter):
      if (product['attributes']['group'] == "VPCE:VpcEndpoint" and
          product['productFamily'] == "VpcEndpoint" and
          product['attributes']['location'] in location_filter and
          product['attributes']['groupDescription'] == "Hourly charge for VPC Endpoints"):
            aws_costs['Region'][product['attributes']['location']]['Product Family'][product['productFamily']][product['attributes']['group']]['VPC Endpoint per hour'] = \
            str(float(vpc_data['terms']['OnDemand'][sku][sku + '.' + hourlyTermCode]['priceDimensions'][sku + '.' + hourlyTermCode + '.' + hourlyRateCode]['pricePerUnit']['USD']))
      if (product['attributes']['location'] in location_filter and
          product['attributes']['groupDescription'] == "Charge for per GB data processed by VPC Endpoints"):
            aws_costs['Region'][product['attributes']['location']]['Product Family'][product['productFamily']][product['attributes']['group']]['Data Processed by VPC Endpoints per GB'] = \
            str(float(vpc_data['terms']['OnDemand'][sku][sku + '.' + hourlyTermCode]['priceDimensions'][sku + '.' + hourlyTermCode + '.' + hourlyRateCode]['pricePerUnit']['USD']))


def return_aws_costs(ec2_products):


  for sku, product in ec2_products.items():
    if (#sku == '7EDGJEQJFK5PT95F' and
        product['productFamily'] == 'Compute Instance' and
        product['attributes']['tenancy'] == 'Shared' and
        product['attributes']['preInstalledSw'] == 'NA' and
        product['attributes']['locationType'] == 'AWS Region' and
        product['attributes']['licenseModel'] != 'Bring your own license' and
        product['attributes']['currentGeneration'] == 'Yes' and
        product['attributes']['location'] in location_filter and
        product['attributes']['operatingSystem'] in operatingSystem_filter and
        product['attributes']['instanceType'] in instanceType_filter):

        aws_costs['Region'][product['attributes']['location']]['Product Family']['Compute Instance']['Operating Systems'][product['attributes']['operatingSystem']][product['attributes']['instanceType']][sku]=ec2_return_prices(sku)
  return aws_costs

def ec2_compose_locations(location_filter):
  loc_dict = {}
  for location in location_filter:
    loc_dict[location] = {[]}
  return loc_dict

## ec2_return_prices returns the prices for a ec2 for a give SKU
def ec2_return_prices(sku):
  prices = {}
  prices['hourly_price'] = str(float(ec2_data['terms']['OnDemand'][sku][sku + '.' + hourlyTermCode]['priceDimensions'][sku + '.' + hourlyTermCode + '.' + hourlyRateCode]['pricePerUnit']['USD']))
  prices['hourly_1y_std_nu'] = ec2_url_for_ri(sku,RI1YRNoUpfrontStdTermCode,hourlyRateCode)
  prices['hourly_1y_std_pu'] = ec2_url_for_ri(sku,RI1YRPartialUpfrontStdTermCode,hourlyRateCode)
  prices['fee_1y_std_pu'] = ec2_url_for_ri(sku,RI1YRPartialUpfrontStdTermCode,upfrontFeeCode)
  prices['hourly_1y_std_au'] = ec2_url_for_ri(sku,RI1YRAllUpfrontStdTermCode,hourlyRateCode)
  prices['fee_1y_std_au'] = ec2_url_for_ri(sku,RI1YRAllUpfrontStdTermCode,upfrontFeeCode)
  prices['hourly_1y_conv_nu'] = ec2_url_for_ri(sku,RI1YRNoUpfrontConvTermCode,hourlyRateCode)
  prices['hourly_1y_conv_pu'] = ec2_url_for_ri(sku,RI1YRPartialUpfrontConvTermCode,hourlyRateCode)
  prices['fee_1y_conv_pu'] = ec2_url_for_ri(sku,RI1YRPartialUpfrontConvTermCode,upfrontFeeCode)
  prices['hourly_1y_conv_au'] = ec2_url_for_ri(sku,RI1YRAllUpfrontConvTermCode,hourlyRateCode)
  prices['fee_1y_conv_au'] = ec2_url_for_ri(sku,RI1YRAllUpfrontConvTermCode,upfrontFeeCode)

  prices['hourly_3y_std_nu'] = ec2_url_for_ri(sku,RI3YRNoUpfrontStdTermCode,hourlyRateCode)
  prices['hourly_3y_std_pu'] = ec2_url_for_ri(sku,RI3YRPartialUpfrontStdTermCode,hourlyRateCode)
  prices['fee_3y_std_pu'] = ec2_url_for_ri(sku,RI3YRPartialUpfrontStdTermCode,upfrontFeeCode)
  prices['hourly_3y_std_au'] = ec2_url_for_ri(sku,RI3YRAllUpfrontStdTermCode,hourlyRateCode)
  prices['fee_3y_std_au'] = ec2_url_for_ri(sku,RI3YRAllUpfrontStdTermCode,upfrontFeeCode)
  prices['hourly_3y_conv_nu'] = ec2_url_for_ri(sku,RI3YRNoUpfrontConvTermCode,hourlyRateCode)
  prices['hourly_3y_conv_pu'] = ec2_url_for_ri(sku,RI3YRPartialUpfrontConvTermCode,hourlyRateCode)
  prices['fee_3y_conv_pu'] = ec2_url_for_ri(sku,RI3YRPartialUpfrontConvTermCode,upfrontFeeCode)
  prices['hourly_3y_conv_au'] = ec2_url_for_ri(sku,RI3YRAllUpfrontConvTermCode,hourlyRateCode)
  prices['fee_3y_conv_au'] = ec2_url_for_ri(sku,RI3YRAllUpfrontConvTermCode,upfrontFeeCode)
  
  return prices


## This function was created to avoid doing this concatenation several times in ec2_return_prices
def ec2_url_for_ri(sku,termcode,costcode):
  try:
    cost = str(float(ec2_data['terms']['Reserved'][sku][sku + '.' + termcode]['priceDimensions'][sku + '.' + termcode + '.' + costcode]['pricePerUnit']['USD']))
  except KeyError:
    cost = "NA"
  return cost

#aws_costs['Region'][location]['Product Family'][productFamily][vpc_product]
#aws_costs['Region'][location]['Product Family']['Compute Instance']['Operating Systems'][operatingSystem][instanceType]

def ec2_pretty_print(ec2_dict):
  open('aws_costs.md','w').close()
  with open('aws_costs.md','w') as file:
    file.write('# Amazon Web Services Costs'+'\n')

    file.write('# Table of contents\n')
    for region,v in ec2_dict.items(): #['Region']
      for region_value,v in v.items(): #region value
        file.write('[**'+region_value+'**](#'+region_value+') \n\n')
        for k,v in v.items(): #['Product Family'] 
          for pf_value,v in v.items(): #product family value
            if (pf_value == 'Data Transfer'):
              file.write('[**Product Family : '+pf_value+'**](#'+pf_value+') \n\n')
            if (pf_value == 'IP Address'):
              file.write('[**Product Family : '+pf_value+'**](#'+pf_value+') \n\n')
            if (pf_value == 'VpcEndpoint'):
              file.write('[**Product Family : '+pf_value+'**](#'+pf_value+') \n\n')
            if (pf_value == 'Cloud Connectivity'):
              file.write('[**Product Family : '+pf_value+'**](#'+pf_value+') \n\n')
            if (pf_value == 'NAT Gateway'):
              file.write('[**Product Family : '+pf_value+'**](#'+pf_value+') \n\n')
            if (pf_value == 'Compute Instance'):
              file.write('[**Product Family : '+pf_value+'**](#'+pf_value+') \n\n')
              for operatingsystems,v in v.items(): #['Operating Systems']
                for os_value,v in v.items():
                  file.write('\n[**'+os_value+'**](#'+os_value+') \n\n')
                  for instance_value,v in v.items():
                    if v:
                      file.write('['+instance_value+'](#'+instance_value+') \n\n')

                  
    for region,v in ec2_dict.items(): #['Region']
      for region_value,v in v.items(): #region value
        print(region+" "+region_value)
        file.write('\n## <a name="'+region_value+'"></a> Region: '+region_value+'\n')
        for k,v in v.items(): #['Product Family'] 
          for pf_value,v in v.items(): #product family value
            if (pf_value == 'Compute Instance'):
              file.write('### <a name="'+pf_value+'"></a> Product Family : '+pf_value+'\n')
              for operatingsystems,v in v.items(): #['Operating Systems']
                for os_value,v in v.items():
                  print(os_value)
                  file.write('#### <a name="'+os_value+'"></a> OS: '+os_value+"\n")
                  for instance_value,v in v.items():
                    if v:
                      file.write('##### <a name="'+instance_value+'"></a> Instance Type: '+instance_value+"\n")
                      print (instance_value)
                      for k,v in v.items():
                        
                        file.write("###### Standard 1 Year Term: \n")
                        file.write("Payment Option  |Upfront                  |Hourly                    |On-Demand Hourly\n")
                        file.write("---             | ---                     |  ---                     | ----\n")
                        file.write("No Upfront      |0                        |"+v['hourly_1y_std_nu']+" |"+v['hourly_price']+"\n")
                        file.write("Partial Upfront |"+v['fee_1y_std_pu']+"   |"+v['hourly_1y_std_pu']+" |^  \n")
                        file.write("Full Upfront    |"+v['fee_1y_std_au']+"   |"+v['hourly_1y_std_au']+" |^ \n")

                        file.write("###### Convertible 1 Year Term: \n")
                        file.write("Payment Option  |Upfront                  |Hourly                    |On-Demand Hourly\n")
                        file.write("---             | ---                     |  ---                     | ----\n")
                        file.write("No Upfront      |0                        |"+v['hourly_1y_conv_nu']+" |"+v['hourly_price']+"\n")
                        file.write("Partial Upfront |"+v['fee_1y_conv_pu']+"   |"+v['hourly_1y_conv_pu']+" |^  \n")
                        file.write("Full Upfront    |"+v['fee_1y_conv_au']+"   |"+v['hourly_1y_conv_au']+" |^ \n")

                        file.write("###### Standard 3 Year Term: \n")
                        file.write("Payment Option  |Upfront                  |Hourly                    |On-Demand Hourly\n")
                        file.write("---             | ---                     |  ---                     | ----\n")
                        file.write("No Upfront      |0                        |"+v['hourly_3y_std_nu']+" |"+v['hourly_price']+"\n")
                        file.write("Partial Upfront |"+v['fee_3y_std_pu']+"   |"+v['hourly_3y_std_pu']+" |^  \n")
                        file.write("Full Upfront    |"+v['fee_3y_std_au']+"   |"+v['hourly_3y_std_au']+" |^ \n")

                        file.write("###### Convertible 3 Year Term: \n")
                        file.write("Payment Option  |Upfront                   |Hourly                    |On-Demand Hourly\n")
                        file.write("---             | ---                      |  ---                     | ----\n")
                        file.write("No Upfront      |0                         |"+v['hourly_3y_conv_nu']+" |"+v['hourly_price']+"\n")
                        file.write("Partial Upfront |"+v['fee_3y_conv_pu']+"   |"+v['hourly_3y_conv_pu']+" |^  \n")
                        file.write("Full Upfront    |"+v['fee_3y_conv_au']+"   |"+v['hourly_3y_conv_au']+" |^ \n")
                        #print(v['hourly_price'])

#aws_costs['Region'][location]['Product Family'][productFamily][vpc_product]
            if (pf_value == 'Data Transfer'):
              print(v)
              file.write('### <a name="'+pf_value+'"></a> Product Family : '+pf_value+'\n\n')
              file.write('#### Data Transfer IN To Amazon EC2 From Internet\n\n')
              file.write('`All data transfer in per GB 0.00 `\n\n')
              file.write('#### Data Transfer OUT From Amazon EC2 From Internet\n\n')
              for k,v in v.items():
                if(k == 'AWS Outbound'):
                  for k,v in v.items():
                    file.write("`"+k+" "+v+'`\n\n')
                if(k == 'IntraRegion'):
                  file.write('#### Data Transfer Across AZ within this Region\n')
                  for k,v in v.items():
                    file.write("`"+k+" "+v+'`\n\n')
            
            if (pf_value == 'IP Address'):
              file.write('### <a name="'+pf_value+'"></a> Product Family : '+pf_value+'\n\n')
              for k,v in v.items():
                for k,v in v.items():
                  file.write("`"+k+" "+v+'`\n\n')
            
            if (pf_value == 'Cloud Connectivity'):
              file.write('### <a name="'+pf_value+'"></a> Product Family : '+pf_value+'\n\n')
              for k,v in v.items():
                for k,v in v.items():
                  file.write("`"+k+" "+v+'`\n\n')

            if (pf_value == 'VpcEndpoint'):
              file.write('### <a name="'+pf_value+'"></a> Product Family : '+pf_value+'\n\n')
              for k,v in v.items():
                for k,v in v.items():
                  file.write("`"+k+" "+v+'`\n\n')

            if (pf_value == 'NAT Gateway'):
              file.write('### <a name="'+pf_value+'"></a> Product Family : '+pf_value+'\n\n')
              for k,v in v.items():
                for k,v in v.items():
                  file.write("`"+k+" "+v+'`\n\n')




#vpc
#Data Transfer IN To Amazon EC2 From Internet
#All data transfer in 0

#Data Transfer OUT From Amazon EC2 To Internet
#Up to 1 GB / Month
#Next 9.999 TB / Month
#Next 40 TB / Month
#Next 100 TB / Month
#Greater than 150 TB / Month

#Data Transfer Across AZ within this Region
#Data transferred "in" to and "out" of Amazon EC2, Amazon RDS, Amazon Redshift , Amazon DynamoDB Accelerator (DAX), and Amazon ElastiCache instances or Elastic Network Interfaces across VPC peering connections in the same AWS region is charged at $0.01/GB.
#Data transferred "in" to and "out" of Amazon Elastic Load Balancing is priced equivalent to Amazon EC2. Data processed by Amazon Elastic Load Balancing will incur charges in addition to Amazon EC2 data transfer charges.
#Using a public or Elastic IPv4 address is charged at $0.01/GB.
#Using an IPv6 address from a different VPC is charged at $0.01/GB.
#Amazon EC2, Amazon RDS, Amazon Redshift and Amazon ElastiCache instances or Elastic Network Interfaces in the same Availability Zone is $0.00/GB.

#All data transfer in and out within the region	



def main():
  init_dict()
  return_aws_costs(ec2_products)
  return_aws_network_costs(vpc_products,ec2_products)
  ec2_pretty_print(aws_costs)

if __name__ == '__main__':
  main()