// function ProcessRequestTestWrapper {
//   input FoiaTestCasePayload
//   output FOIARequestData
// }

// function ProcessRequestMetadataTestWrapper {
//   input FoiaTestCasePayload
//   output FOIARequestData
// }

// class FoiaTestCasePayload {
//   name  string
//   tid   int
//   cid   int
//   username  string
//   communication string?
//   file_text string?
//   status string?
//   tracking_number string?
//   date_estimate string?
//   price float?
// }

// impl<code, ProcessRequestTestWrapper> v1 {
//   @method impl {
//     @lang[py] {
//       async def impl(input: InputType) -> OutputType:
//         from app import process_request_test
//         res = await process_request_test(input)
//         return res
//     } 
//   }
// }

// impl<code, ProcessRequestMetadataTestWrapper> v1 {
//   @method impl {
//     @lang[py] {
//       async def impl(input: InputType) -> OutputType:
//         from app import process_request_metadata_test
//         res = await process_request_metadata_test(input)
//         return res
//     } 
//   }
// }
