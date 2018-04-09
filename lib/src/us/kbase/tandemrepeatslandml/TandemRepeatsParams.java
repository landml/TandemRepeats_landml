
package us.kbase.tandemrepeatslandml;

import java.util.HashMap;
import java.util.Map;
import javax.annotation.Generated;
import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonAnySetter;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * <p>Original spec-file type: TandemRepeatsParams</p>
 * <pre>
 * A 'typedef' can also be used to define compound or container
 * objects, like lists, maps, and structures.  The standard KBase
 * convention is to use structures, as shown here, to define the
 * input and output of your function.  Here the input is a
 * reference to the Assembly data object, a workspace to save
 * output, and a length threshold for filtering.
 * To define lists and maps, use a syntax similar to C++ templates
 * to indicate the type contained in the list or map.  For example:
 *     list <string> list_of_strings;
 *     mapping <string, int> map_of_ints;
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "assembly_input_ref",
    "workspace_name",
    "max_period_size"
})
public class TandemRepeatsParams {

    @JsonProperty("assembly_input_ref")
    private String assemblyInputRef;
    @JsonProperty("workspace_name")
    private String workspaceName;
    @JsonProperty("max_period_size")
    private Long maxPeriodSize;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("assembly_input_ref")
    public String getAssemblyInputRef() {
        return assemblyInputRef;
    }

    @JsonProperty("assembly_input_ref")
    public void setAssemblyInputRef(String assemblyInputRef) {
        this.assemblyInputRef = assemblyInputRef;
    }

    public TandemRepeatsParams withAssemblyInputRef(String assemblyInputRef) {
        this.assemblyInputRef = assemblyInputRef;
        return this;
    }

    @JsonProperty("workspace_name")
    public String getWorkspaceName() {
        return workspaceName;
    }

    @JsonProperty("workspace_name")
    public void setWorkspaceName(String workspaceName) {
        this.workspaceName = workspaceName;
    }

    public TandemRepeatsParams withWorkspaceName(String workspaceName) {
        this.workspaceName = workspaceName;
        return this;
    }

    @JsonProperty("max_period_size")
    public Long getMaxPeriodSize() {
        return maxPeriodSize;
    }

    @JsonProperty("max_period_size")
    public void setMaxPeriodSize(Long maxPeriodSize) {
        this.maxPeriodSize = maxPeriodSize;
    }

    public TandemRepeatsParams withMaxPeriodSize(Long maxPeriodSize) {
        this.maxPeriodSize = maxPeriodSize;
        return this;
    }

    @JsonAnyGetter
    public Map<String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    @JsonAnySetter
    public void setAdditionalProperties(String name, Object value) {
        this.additionalProperties.put(name, value);
    }

    @Override
    public String toString() {
        return ((((((((("TandemRepeatsParams"+" [assemblyInputRef=")+ assemblyInputRef)+", workspaceName=")+ workspaceName)+", maxPeriodSize=")+ maxPeriodSize)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
