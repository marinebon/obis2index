# loads data from obis & saves results to csv

library("glue")

# === variables
FKNMS_WKT <- "POLYGON((-83.15 25.65, -80.066667 25.65, -80.066667 24.3, -83.15 24.3, -83.15 25.65))"
obis_records_file <- 'data/top_mofs-FKNMS.csv'
obis_mofs_file <- 'data/top_mofs-FKNMS_mofs.csv'

# data query cache setup:
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

# === fetch data from area
if (has_cache(obis_records_file)){
    obis_records <- read.csv(obis_records_file)
} else {
    obis_records <- robis::occurrence(
        geometry = FKNMS_WKT,
        mof = TRUE,
        fields    = c(
            'occurrenceID', 'date_year', 'habitat', 'scientificName', 'aphiaID',
            'decimalLatitude', 'decimalLongitude', 'occurrenceStatus',
            'basisOfRecord', 'date_start', 'date_mid', 'date_end',
            'samplingProtocol', 'recordedBy',
            'maximumDepthInMeters', 'minimumDepthInMeters', 'dataset_id',
            'eventDate', 'datasetName', 'coordinateUncertaintyInMeters',
            'ownerInstitutionCode', 'samplingEffort', 'depth', 'individualCount'
        )
    )
    # TODO: check for each of the columns we need b/c API doesn't fail on empty
    obis_records_chars <- apply(obis_records,2,as.character)  # convert lists and other non-csv friendly cols
    write.csv(obis_records_chars, file = obis_records_file)
}

# === fetch measurement or facts
if (has_cache(obis_mofs_file)){
    obis_mofs <- read.csv(obis_mofs_file)
} else {
    obis_mofs <- robis::measurements(
        obis_records
    )
    write.csv(obis_mofs, file = obis_mofs_file)
}
