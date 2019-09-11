library(methods)
options(repos = c(CRAN = "https://mirrors.tuna.tsinghua.edu.cn/CRAN"))

if (!identical(Sys.getenv("RSTUDIO"), "1")) {
  options(device_args = list())
  options(device_call = function(filename, ...) {
    device_args <- c(filename = filename, getOption("device_args", list()))
    do.call("png", device_args)
  })
  options(device = function(...) {
    dir <- ".images"
    dir.create(dir, showWarnings = FALSE)
    cur_file <- file.path(dir, "latest.png")
    if (file.exists(cur_file)) {
      bak_file <- file.path(dir, format(Sys.time(), "%Y%m%d-%H%M%S.png"))
      file.copy(cur_file, bak_file)
    }
    device_call <- getOption("device_call")
    device_call(filename = cur_file, ...)
  })
}
