#!/usr/bin/env python3

from diagrams import Diagram, Cluster
from diagrams.aws.compute import ECS
from diagrams.aws.database import Aurora
from diagrams.aws.network import ELB, CF

with Diagram("Example Architecture", show=False, direction="TB"):
    cf = CF('CloudFront')
    elb = ELB('ALB')

    admin_elb = ELB('Admin ELB')

    with Cluster('ECS Cluster'):
        ecs_cluster = [ECS('ECS1'), ECS('ECS2')]

    with Cluster('ECS Admin Cluster'):
        admin_cluster = [ECS('ECS1'), ECS('ECS2')]

    with Cluster('Aurora Cluster'):
        master = Aurora('master')
        slave = Aurora('slave')
        master - slave

    cf >> elb >> ecs_cluster >> master
    admin_elb >> admin_cluster >> master
