resource "aws_instance" "instance" {
  ami           = "ami-0ff338189efb7ed37"
  instance_type = "t3.micro"
  key_name      = "lab4"
  tags = {
    Name = "Web server by TerraForm"
  }
}
output "my-public-ip" {
  value = aws_instance.instance.public_ip
}