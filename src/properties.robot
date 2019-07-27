*** Variables ***
${mainUrl}  https://jsonplaceholder.typicode.com
${end_point_posts}  ${mainUrl}/posts
${end_point_posts_1}  ${end_point_posts}/1
${OK_status}  200
${number_of_records_posts}  100
${number_of_records_posts_1}  1
${input_id}  1
${invalid_url}   ${main_url}/invalidposts
${invalid_status}  404
${post_request_body}  "{'title': 'foo','body': 'bar','userId': 1}"
${put_request_body}  "{'id': 1,'title': 'abc',  'body': 'xyz','userId':1}"
${post_status_code}  201
${put_status_code}  200
