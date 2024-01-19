function ExtractRequestData {
  input string
  output FOIARequestData
}

class FOIARequestData {
  trackingNumber string?
  dateEstimate string?
  price float?
  priceDetails string?
  reasoning string
  requestStatus RequestStatus
  recordsStatus RecordsStatus
}

enum RecordsStatus { 
  NOT_APPLICABLE
  RECORDS_FOUND
  NO_RECORDS_FOUND 
  MORE_RECORDS_PENDING
}
 
enum RequestStatus {
  IN_PROGRESS 
  FIX_REQUIRED
  PAYMENT_REQUIRED
  REQUEST_REJECTED
  REQUEST_COMPLETED
  INDETERMINATE
}

impl<llm, ExtractRequestData> v1 {
  client GPT4Client

  override FOIARequestData {
    dateEstimate
    @description("An ISO8601 string of the date by which the agency estimates it will complete processing the request. Use null if not present.")

    price
    @description("The total balance remaining to pay for this request, as a float. Use null if not present.")

    priceDetails
    @description("A sentence describing what the price is for (e.g. per page or record delivered, etc). null if not present.")
  }

  override RequestStatus {
    IN_PROGRESS
    @description("The agency accepted the request and is working on it. Use this status if the agency still has more work to do or has records pending, and the status doesn't fit any other status.")

    FIX_REQUIRED
    @description("The agency has asked the requestor for clarification, to supply additional information, to narrow down a request, or complete an additional task (not including forwarding the request to another agency or interacting with online portal systems) in order to allow them to continue processing the request")

    PAYMENT_REQUIRED
    @description("The requestor must pay a fee for the agency to continue processing.")

    REQUEST_REJECTED
    @description("The request has been denied due to legal exemptions, an issue with the request such as it not being specific enough, the request should be forwarded to another agency, or another reason which causes them not to be able to process it.")

    REQUEST_COMPLETED
    @description("The agency has completed their processing of the request, and has attached any responsive documents (possibly redacted) found, if there are any. Only use this if there is nothing else left to do for either party.")

    INDETERMINATE
    @description("Use this status if you cannot determine the correct status from the information provided or if the communication is not related to a public records request.")
  }

  override RecordsStatus {
    MORE_RECORDS_PENDING
    @description("The agency has indicated that there are more records to be released soon for this request")

    NO_RECORDS_FOUND
    @description("The agency has indicated that there are no records found for this request")

    RECORDS_FOUND
    @description("The agency has indicated that there are records found for this request")

    NOT_APPLICABLE
    @description("The text does not match any other record status. It may be that the request is still in progress.")
  }

  prompt #"
    You are analyzing public records correspondence to figure out what the status of the request for public records is. Your job is to extract the information from the government's response and classify the status of the request.
         
    For the requestStatus field, use the following definitions:
    {#print_enum(RequestStatus)}
 
    For the recordsStatus field, use the following definitions:
    {#print_enum(RecordsStatus)}

    Agency's response to user:
    ###
    {#input}
    ###

    OUTPUT FORMAT:
    {#print_type(output)}

    JSON:
  "#
}