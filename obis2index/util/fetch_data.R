# this function fetches occurrence and measurement or fact data from OBIS
# saves both to csv files and returns the dataframes.
# The Florida Keys National Marine Sanctuary poly is hard-coded here and
# used as a default but can be overriden by passing in a different roi_wkt.

library(glue)
source('obis2index/util/has_cache.R')

FILEPATH_PREFIX <- "data/FKNMS"
FKNMS_WKT <- "POLYGON((-83.15 25.65, -80.066667 25.65, -80.066667 24.3, -83.15 24.3, -83.15 25.65))"

fetch_data_multispecies <- function(
    filepath_id,
    scientific_names,
    roi_wkt=FKNMS_WKT,
    start_date=NULL, end_date=NULL,
    measurement_type=NULL
){
    obis_records_file <- glue('{FILEPATH_PREFIX}-{filepath_id}-ocr.csv')
    obis_mofs_file <- glue('{FILEPATH_PREFIX}-{filepath_id}-mof.csv')
    if (has_cache(obis_records_file) & has_cache(obis_mofs_file)){
        obis_records <- read.csv(obis_records_file)
        obis_mofs <- read.csv(obis_mofs_file)
    }else{
        for(species in scientific_names){
            list[this_obis_records, this_obis_mofs] = fetch_data(
                species, roi_wkt, start_date, end_date, measurement_type
            )
            obis_records <- rbind(obis_records, this_obis_records)
            obis_mofs <- rbind(obis_mofs, this_obis_mofs)
        }
        # convert lists and other non-csv friendly cols
        obis_records_chars <- apply(obis_records, 2, as.character)
        write.csv(obis_records_chars, file = obis_records_file)
        write.csv(obis_mofs, file = obis_mofs_file)
    }
    return c(obis_records, obis_mofs)
}


fetch_data <- function(
    filepath_id,
    roi_wkt=FKNMS_WKT,
    start_date=NULL, end_date=NULL,
    measurement_type=NULL,
    scientific_name = NULL
){
    obis_records_file <- glue('{FILEPATH_PREFIX}-{filepath_id}-ocr.csv')
    obis_mofs_file    <- glue('{FILEPATH_PREFIX}-{filepath_id}-mof.csv')
    # === fetch data from area
    if (has_cache(obis_records_file)){
        obis_records <- read.csv(obis_records_file)
    } else {
        obis_records <- robis::occurrence(
            geometry = roi_wkt,
            mof = TRUE,
            scientificname = scientific_name,
            startdate = start_date,
            enddate = end_date,
            measurementtype = measurement_type,
            fields = c(
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
    return c(obis_records, obis_mofs)
}
