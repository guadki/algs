name := "algs"

version := "0.1"

scalaVersion := "2.13.2"

lazy val root = (project in file("."))
  .settings(
    name := "helloSBT",
    libraryDependencies += "org.scalatest" %% "scalatest" % "3.1.1" % "test",
    libraryDependencies += "org.scalacheck" %% "scalacheck" % "1.14.1" % "test"
  )
