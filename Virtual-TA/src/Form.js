import React, { useState, useEffect } from "react";
import { Form, Input } from "antd";
import "antd/dist/antd.css";
import { MathJax, MathJaxContext } from "better-react-mathjax";

const sampleEquation1 = "`U = 1/(R_(si) + sum_(i=1)^n(s_n/lambda_n) + R_(se))`";
const sampleEquation2 = "c = a^2 + b^2";
const sampleEquation3 =
  "f(a) = 1/(R_(si) + sum_(i=1)^n(s_n/lambda_n) + R_(se))";
  const conf = {
    loader: { load: ["input/asciimath"] },
    asciimath: {
      displaystyle: true,
      delimiters: [
        ["$", "$"],
        ["`", "`"]
      ]
    }
  };
export default function MathForm() {
  const [equation, setEquation] =  useState(sampleEquation1);

  const [form] = Form.useForm();

  return (
    <div className="App" style={{ padding: 16 }}>
      <Form
        form={form}
        onValuesChange={(changedValue) => {
          setEquation(changedValue.equation);
        }}
      >
        <Form.Item name="equation" initialValue={equation}>
          <Input.TextArea />
        </Form.Item>      </Form>
        <div>Preview:</div>
        <div>
        <MathJaxContext config={conf}><MathJax inline>{equation}</MathJax></MathJaxContext>
        </div>
        This is where I will put the legend for MathJax

    </div>
  );
}
