import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Register from "./pages/Register";
import Student from "./pages/Student";
import NotFound from "./pages/NotFound";
function App() {
  return (
    <>
      <Router>
        <Routes>
          <Route path="*" element={<NotFound />} />
          <Route path="/" element={<Register />} />
          <Route path="/student/" element={<Student />} />
        </Routes>
      </Router>
    </>
  );
}

export default App;
