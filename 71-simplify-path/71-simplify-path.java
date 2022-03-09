class Solution {
    public String simplifyPath(String path) {
        Stack<String> stack = new Stack<>();
        String[] parts = path.split("/");
        for (String part: parts) {
            if (part.equals("..")) {
                if (!stack.empty()) {
                    stack.pop();
                }
            } else if (part.equals(".") || part.equals("")) {
                continue;
            } else {
                stack.push(part);
            }
        }
        
        String result = "";
        Iterator s = stack.iterator();
        while (s.hasNext()) {
            result += "/" + s.next();
        }
        if (result.equals("")) {
            result = "/";
        }
        return result;
    }
}