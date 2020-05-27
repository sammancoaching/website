---
layout: default
title: Approval Testing in a Microservices Architecture
parent: Approval Testing
grand_parent: Workshops
nav_order: 4
---

# Approval Testing with Microservices

Microservices is a popular architectural choice today, and it opens up new possibilities for automated testing. We will look at how you could use Approval testing to:

- test one microservice via its api
- test a group of microservices fulfilling a whole user-perspective scenario

We will work in small groups to write tests for an example microservice application. 


## Session Outline

* Connect: have you worked with microservices?



## What I'd like to do

* introduce what microservices are in general
* exercise - write some approval tests for a single microservice running on its own. Possibly with stubbed out access to other services. At present I'm working on using [Restful booker](https://github.com/emilybache/restful-booker) for this. I have a branch 'with_texttests' which is looking promising. I think I can get this working soon.
* explain my experience testing several microservices together at Pagero. I have some slides for this from a previous presentation
* exercise - write some approval tests for several microservices all running together. Using texttest. Use jaeger tracing as part of the test baseline and for debugging. This part is much less prepared. I have found a demo application "Hot ROD" which is the demo for the book "Mastering Distributed Tracing" by Yuri Shkuro. I am evaluating whether I could use it. I am also looking at a more extensive application which is more fun and has more test-possibilities [Robot Shop](https://github.com/emilybache/robot-shop). That one uses instana for tracing instead of jaeger. I'd prefer to use jaeger though. Another idea is to write my own demo application which is optimized for demoing exactly the thing I want to show - that is, debugging a test case using distributed tracing.

## Notes

Get Jaeger and the example application from this page: https://github.com/jaegertracing/jaeger/releases/tag/v1.6.0/. Unzip it somewhere

	tar xvfz jaeger-1.6.0-darwin-amd64.tar.gz

