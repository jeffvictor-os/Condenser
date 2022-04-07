resource "aws_subnet" "condenser-subnet" {
  vpc_id = "${aws_vpc.condenser-vpc.id}"
  cidr_block = "10.0.1.0/24"
  map_public_ip_on_launch = "true"
  availability_zone = "us-east-2a"
  tags = {
      Name = "condenser-subnet"
  }
}

resource "aws_internet_gateway" "condenser-igw" {
  vpc_id = "${aws_vpc.condenser-vpc.id}"
  tags = {
      Name = "condenser-igw"
  }
}

resource "aws_route_table" "condenser-rt" {
  vpc_id = "${aws_vpc.condenser-vpc.id}"

  route {
      # Subnet can reach the Internet
      cidr_block = "0.0.0.0/0"
      # Route table uses the IGW to reach the Internet
      gateway_id = "${aws_internet_gateway.condenser-igw.id}"
  }
  tags = {
      Name = "condenser-rt"
  }
}

resource "aws_route_table_association" "condenser-rta-subnet"{
  subnet_id = "${aws_subnet.condenser-subnet.id}"
  route_table_id = "${aws_route_table.condenser-rt.id}"
}
