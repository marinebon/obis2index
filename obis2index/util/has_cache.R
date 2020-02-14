has_cache <- function(
    fpath
){
    # returns true if given query id is cached
    if (file.exists(fpath)){
        return(TRUE)
    } else {
        return(FALSE)
    }
}
