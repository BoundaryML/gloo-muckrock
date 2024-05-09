function PaymentValidation {
    input string
    output PaymentValidationData
}

class ExactPaymentData {
    exactAmount float
    quote string
}

class EstimatePaymentData {
    estimateAmount float
    quote string
}

class ReceivedPaymentData {
    paymentNotReceived bool
    quote string
}
 
class PaymentValidationData2 {
    estimate string? @description("Only set if the payment refers to an estimate but not an exact guidance.  Future work is always an estimate.")
    exact float? @description("If the email is outlining exactly what the final payment due is.")
    notReceived string? @description("The exact quote in the email explicitly stating a previously requested payment has not been received yet.")
}

class PaymentValidationData3 {
    presentPayment float? @description("If the agency is asking for a payment to be made now to fulfill the current request - include estimates which must be paid before they will begin working on the request.")
    futurePayment float? @description("If the agency is giving an estimate or advanced notice for an amount which will be due in the future, and does not need to be made now.")
    notReceived bool @description("Is the agency stating they have not yet received payment which was previously asked for.  This should only be true for follow ups to previous requests for payment or invoices, and not for new payment requests.")
}

class PaymentValidationData {
    paymentAmount float? @description("The amount of money the agency is requesting, if they have given an amount")
    estimate bool @description("Is the amount of money being requested an estimate?  This is opposed to it being an exact amount.")
    required bool @description("Is the payment required now, before they will process the request, whether it is an estimate of the final cost or not, or is it just a notice that payment will be required in the future?")
    responseRequired bool @description("If the payment is required before they will process the request, are they asking for any sort of response before accepting payment, such as how you would like to proceed, confirmation to proceed, if you accept the charges, need to choose between versions of the request, or any other modifications of the request?")
    notReceived bool @description("Is the agency stating they have not yet received payment which was previously asked for.  This should only be true for follow ups to previous requests for payment or invoices, and not for new payment requests.")
}

impl<llm, PaymentValidation> v1 {
    client GPT4Client

    prompt #"
        Given this email extract any payment related content

        ###
        {#input}
        ###

        OUTPUT FORMAT:
        {#print_type(output)}

        Before OUTPUT FORMAT, summarize all the payment related content.
        Example: 
        <summary...>
        {
            ...
        }
    "#
}


