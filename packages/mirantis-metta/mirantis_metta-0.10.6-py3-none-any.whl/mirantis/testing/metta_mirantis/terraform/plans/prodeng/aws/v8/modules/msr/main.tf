locals {
  tags = merge(
    var.tags,
    {
      "Name" = "${var.constants.cluster_name}-${var.node_role}"
      "Role" = var.node_role
    }
  )
  os_type = "linux"
}

resource "aws_security_group" "node" {
  name        = "${var.constants.cluster_name}-${var.node_role}s"
  description = "MKE cluster ${var.node_role}s"
  vpc_id      = var.globals.vpc_id

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = var.tags
}

module "spot" {
  source        = "../spot"
  node_count    = var.node_count
  instance_type = var.node_instance_type
  node_role     = var.node_role
  volume_size   = var.node_volume_size
  asg_node_id   = aws_security_group.node.id
  os_type       = local.os_type
  constants     = var.constants
  globals       = var.globals
  tags          = local.tags
}
