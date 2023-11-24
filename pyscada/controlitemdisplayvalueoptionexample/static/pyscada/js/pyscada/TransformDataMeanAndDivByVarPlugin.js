function PyScadaControlItemDisplayValueTransformDataMeanAndDivByVar(key, val, control_item_id, display_value_option_id, transform_data_id) {
  var variable_id = get_config_from_hidden_config('controlitem', 'display-value-options', displayvalueoption_id, 'variable');
  if (DATA[variable_id] == undefined) {
    console.log("PyScada HMI : PyScadaControlItemDisplayValueTransformDataMeanAndDivByVar : " + variable_id + " not in DATA. ")
    return val;
  }
  var data = sliceDATAusingTimestamps(variable_id);
  if (data.length > 0) {
    var result = 0;
    for (d in data) {
      result = result + data[d][1];
    }
    result = result / data.length;
    var variable2_id = get_config_from_hidden_config('transformdatameananddivbyvar', 'display-value-option', displayvalueoption_id, 'variable');
    var data2 = sliceDATAusingTimestamps(variable2_id);
    if (variable2_id in DATA && data2.length > 0) {
      result = result / data2[data2.length - 1][1];
      return result;
    }else {
      console.log("PyScada HMI : PyScadaControlItemDisplayValueTransformDataMeanAndDivByVar : DATA[" + variable2_id + "].length = 0. ");
      return val;
    }
  }else {
    console.log("PyScada HMI : PyScadaControlItemDisplayValueTransformDataMeanAndDivByVar : DATA[" + variable_id + "].length = 0. ");
    return val;
  }
}

// After PyScada Core JS loaded, add the "div by variable" needed by MeanAndDivByVar to STATUS_VARIABLE_KEYS
document.addEventListener("PyScadaCoreJSLoaded", (event) => {
  document.querySelectorAll(".transformdatameananddivbyvar-config2").forEach(e => {
    if (e.dataset["variable"]) {
      STATUS_VARIABLE_KEYS[e.dataset["variable"]] = 0;
    }
  });
});
