resource "aws_security_group" "manager" {
  name        = "${var.cluster_name}-managers"
  description = "mke cluster managers"
  vpc_id      = var.vpc_id

  ingress {
    from_port = 2379
    to_port   = 2380
    protocol  = "tcp"
    self      = true
  }

  ingress {
    from_port   = var.controller_port
    to_port     = var.controller_port
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 6443
    to_port     = 6443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

locals {
  subnet_count = length(var.subnet_ids)
}

resource "aws_instance" "mke_manager" {
  count = var.manager_count

  tags = {
    "Name"                 = "${var.cluster_name}-manager-${count.index + 1}"
    "Role"                 = "manager"
    (var.kube_cluster_tag) = "shared"
    "project"              = var.project
    "platform"             = var.platform
    "expire"               = var.expire
  }

  instance_type          = var.manager_type
  iam_instance_profile   = var.instance_profile_name
  ami                    = var.image_id
  key_name               = var.ssh_key
  vpc_security_group_ids = [var.security_group_id, aws_security_group.manager.id]
  subnet_id              = var.subnet_ids[count.index % local.subnet_count]
  ebs_optimized          = true
  user_data              = <<EOF
#!/bin/bash
# Use full qualified private DNS name for the host name.  Kube wants it this way.
HOSTNAME=$(curl http://169.254.169.254/latest/meta-data/hostname)
echo $HOSTNAME > /etc/hostname
grep -q $HOSTNAME /etc/hosts || sed -ie "s|\(^127\.0\..\.. .*$\)|\1 $HOSTNAME|" /etc/hosts
hostname $HOSTNAME
EOF

  lifecycle {
    ignore_changes = [ami]
  }

  root_block_device {
    volume_type = "gp2"
    volume_size = var.manager_volume_size
  }
}

resource "aws_lb" "mke_manager" {
  name               = "${var.cluster_name}-manager-lb"
  internal           = false
  load_balancer_type = "network"
  subnets            = var.subnet_ids

  tags = {
    "Name"                 = var.cluster_name
    "Role"                 = "manager"
    (var.kube_cluster_tag) = "shared"
    "project"              = var.project
    "expire"               = var.expire
  }
}

resource "aws_lb_target_group" "mke_manager_api" {
  name     = "${var.cluster_name}-api"
  port     = var.controller_port
  protocol = "TCP"
  vpc_id   = var.vpc_id
}

resource "aws_lb_listener" "mke_manager_api" {
  load_balancer_arn = aws_lb.mke_manager.arn
  port              = var.controller_port
  protocol          = "TCP"

  default_action {
    target_group_arn = aws_lb_target_group.mke_manager_api.arn
    type             = "forward"
  }
}

resource "aws_lb_target_group_attachment" "mke_manager_api" {
  count            = var.manager_count
  target_group_arn = aws_lb_target_group.mke_manager_api.arn
  target_id        = aws_instance.mke_manager[count.index].id
  port             = var.controller_port
}

resource "aws_lb_target_group" "mke_kube_api" {
  name     = "${var.cluster_name}-kube-api"
  port     = 6443
  protocol = "TCP"
  vpc_id   = var.vpc_id
}

resource "aws_lb_listener" "mke_kube_api" {
  load_balancer_arn = aws_lb.mke_manager.arn
  port              = 6443
  protocol          = "TCP"

  default_action {
    target_group_arn = aws_lb_target_group.mke_kube_api.arn
    type             = "forward"
  }
}

resource "aws_lb_target_group_attachment" "mke_kube_api" {
  count            = var.manager_count
  target_group_arn = aws_lb_target_group.mke_kube_api.arn
  target_id        = aws_instance.mke_manager[count.index].id
  port             = 6443
}
