source('obis2index/util/fetch_data.R')

filepath_id = 'everything'
obis_records_file <- glue('{FILEPATH_PREFIX}-{filepath_id}-ocr.csv')

# === fetch measurement or facts
if (has_cache(obis_records_file)){
    obis_mofs <- read.csv(obis_records_file)
} else {
    obis_records <- robis::occurrence(
        geometry = FKNMS_WKT
    )
    write.csv(obis_mofs, file = obis_records_file)
}
