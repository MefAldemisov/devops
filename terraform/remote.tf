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
      "cd /var/www/html/web/",
      "sudo git clone https://github.com/MefAldemisov/devops.git",
      "cd /var/www/html/web/devops/app_python/",
      "pip install -r requirements.txt",
      "flask run --host 0.0.0.0 --port 5000",
    ]
    on_failure = continue
  }
}