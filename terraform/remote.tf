resource "null_resource" "remote" {
  connection {
    type        = "ssh"
    user        = "ec2-user"
    private_key = file("../lab4.pem")
    host        = aws_instance.instance.public_ip
  }
  provisioner "remote-exec" {
    inline = [
      "sudo yum install git -y",
      "sudo git clone https://github.com/MefAldemisov/devops.git /var/www/html/web/",
      "cd /var/www/html/web/app_python/",
      "pip install -r requirements.txt",
      "flask run --host 0.0.0.0 --port 5000",
      "docker-compose up"
    ]
    on_failure = "continue"
  }
}