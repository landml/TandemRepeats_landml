
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
    "match_weight",
    "mismatch_weight",
    "delta_weight",
    "prob_pm",
    "prob_pi",
    "min_score",
    "max_period_size"
})
public class TandemRepeatsParams {

    @JsonProperty("assembly_input_ref")
    private String assemblyInputRef;
    @JsonProperty("workspace_name")
    private String workspaceName;
    @JsonProperty("match_weight")
    private Long matchWeight;
    @JsonProperty("mismatch_weight")
    private Long mismatchWeight;
    @JsonProperty("delta_weight")
    private Long deltaWeight;
    @JsonProperty("prob_pm")
    private Long probPm;
    @JsonProperty("prob_pi")
    private Long probPi;
    @JsonProperty("min_score")
    private Long minScore;
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

    @JsonProperty("match_weight")
    public Long getMatchWeight() {
        return matchWeight;
    }

    @JsonProperty("match_weight")
    public void setMatchWeight(Long matchWeight) {
        this.matchWeight = matchWeight;
    }

    public TandemRepeatsParams withMatchWeight(Long matchWeight) {
        this.matchWeight = matchWeight;
        return this;
    }

    @JsonProperty("mismatch_weight")
    public Long getMismatchWeight() {
        return mismatchWeight;
    }

    @JsonProperty("mismatch_weight")
    public void setMismatchWeight(Long mismatchWeight) {
        this.mismatchWeight = mismatchWeight;
    }

    public TandemRepeatsParams withMismatchWeight(Long mismatchWeight) {
        this.mismatchWeight = mismatchWeight;
        return this;
    }

    @JsonProperty("delta_weight")
    public Long getDeltaWeight() {
        return deltaWeight;
    }

    @JsonProperty("delta_weight")
    public void setDeltaWeight(Long deltaWeight) {
        this.deltaWeight = deltaWeight;
    }

    public TandemRepeatsParams withDeltaWeight(Long deltaWeight) {
        this.deltaWeight = deltaWeight;
        return this;
    }

    @JsonProperty("prob_pm")
    public Long getProbPm() {
        return probPm;
    }

    @JsonProperty("prob_pm")
    public void setProbPm(Long probPm) {
        this.probPm = probPm;
    }

    public TandemRepeatsParams withProbPm(Long probPm) {
        this.probPm = probPm;
        return this;
    }

    @JsonProperty("prob_pi")
    public Long getProbPi() {
        return probPi;
    }

    @JsonProperty("prob_pi")
    public void setProbPi(Long probPi) {
        this.probPi = probPi;
    }

    public TandemRepeatsParams withProbPi(Long probPi) {
        this.probPi = probPi;
        return this;
    }

    @JsonProperty("min_score")
    public Long getMinScore() {
        return minScore;
    }

    @JsonProperty("min_score")
    public void setMinScore(Long minScore) {
        this.minScore = minScore;
    }

    public TandemRepeatsParams withMinScore(Long minScore) {
        this.minScore = minScore;
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
        return ((((((((((((((((((((("TandemRepeatsParams"+" [assemblyInputRef=")+ assemblyInputRef)+", workspaceName=")+ workspaceName)+", matchWeight=")+ matchWeight)+", mismatchWeight=")+ mismatchWeight)+", deltaWeight=")+ deltaWeight)+", probPm=")+ probPm)+", probPi=")+ probPi)+", minScore=")+ minScore)+", maxPeriodSize=")+ maxPeriodSize)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
