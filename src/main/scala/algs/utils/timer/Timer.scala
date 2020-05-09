package algs.utils.timer

trait Timer {
  def time[R](tag: String)(block: => R): R = {
    val t0 = System.nanoTime()
    val result = block
    val t1 = System.nanoTime()
    println(s"[$tag] Elapsed time: ${t1 - t0} ns")
    result
  }
}
