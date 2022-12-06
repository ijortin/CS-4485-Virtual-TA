import React from "react";
import { Table } from "antd";
import "antd/dist/antd.css";
import { MathJax, MathJaxContext } from "better-react-mathjax";
//create config options to define latex delimiters
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
//create table entries
  const dataSource = [
    {
      key: '1',
      equation: 'log_(x)',
      example:<MathJaxContext config={conf}> <MathJax inline>{"$log_x$"}</MathJax></MathJaxContext>,
    },
    {
      key: '2',
      equation: 'sum_(i=1)^n',
      example:<MathJaxContext config={conf}> <MathJax inline>{"$sum_(i=1)^n$"}</MathJax></MathJaxContext>,
    },
    {
      key: '3',
      equation: 'oo',
      example:<MathJaxContext config={conf}> <MathJax inline>{"$oo$"}</MathJax></MathJaxContext>,
    },
    {
      key: '4',
      equation: 'sqrt(x)',
      example:<MathJaxContext config={conf}> <MathJax inline>{"$sqrt(x)$"}</MathJax></MathJaxContext>,
    },
    {
      key: '5',
      equation: 'root(y)(x)',
      example:<MathJaxContext config={conf}> <MathJax inline>{"$root(y)(x)$"}</MathJax></MathJaxContext>,
    },
    {
      key: '6',
      equation: 'and/or/not',
      example:<MathJaxContext config={conf}> <MathJax inline>{"$(notAorB)andC$"}</MathJax></MathJaxContext>,
    },
    {
      key: '7',
      equation: 'sin(x)/cos(x)/tan(x)',
      example:<MathJaxContext config={conf}> <MathJax inline>{"$sin(x)  cos(x)  tan(x)$"}</MathJax></MathJaxContext>,
    },
    {
      key: '8',
      equation: 'sin(x)/cos(x)/tan(x)',
      example:<MathJaxContext config={conf}> <MathJax inline>{"$sin(x)  cos(x)  tan(x)$"}</MathJax></MathJaxContext>,
    },
    {
      key: '9',
      equation: 'sec(x)/csc(x)/cot(x)',
      example:<MathJaxContext config={conf}> <MathJax inline>{"$sec(x)  csc(x)  cot(x)$"}</MathJax></MathJaxContext>,
    },
    {
      key: '10',
      equation: '!=',
      example:<MathJaxContext config={conf}> <MathJax inline>{"$!=$"}</MathJax></MathJaxContext>,
    },
    {
      key: '11',
      equation: 'exp(x)',
      example:<MathJaxContext config={conf}> <MathJax inline>{"$exp(x)$"}</MathJax></MathJaxContext>,
    },
    {
      key: '12',
      equation: 'ln(x)',
      example:<MathJaxContext config={conf}> <MathJax inline>{"$ln(x)$"}</MathJax></MathJaxContext>,
    },
    {
      key: '13',
      equation: '(xmody)',
      example:<MathJaxContext config={conf}> <MathJax inline>{"$(xmody))$"}</MathJax></MathJaxContext>,
    },
    {
      key: '14',
      equation: 'f = mx + b',
      example:<MathJaxContext config={conf}> <MathJax inline>{"$f=mx+b$"}</MathJax></MathJaxContext>,
    },
    {
      key: '15',
      equation: 'theta',
      example:<MathJaxContext config={conf}> <MathJax inline>{"$theta$"}</MathJax></MathJaxContext>,
    },
    {
      key: '16',
      equation: 'Omega',
      example:<MathJaxContext config={conf}> <MathJax inline>{"$Omega$"}</MathJax></MathJaxContext>,
    },
    {
      key: '17',
      equation: 'abs(x)',
      example:<MathJaxContext config={conf}> <MathJax inline>{"$abs(x)$"}</MathJax></MathJaxContext>,
    },
    
  ];
  
  const columns = [
    {
      title: 'Notation',
      dataIndex: 'equation',
      key: 'equation',
    },
    {
      title: 'Display',
      dataIndex: 'example',
      key: 'ex',
    },
  ];
export default function MathForm() {
  return (
    <div className="App" style={{ padding: 16 }}>
        <br></br>
        Guide to equation input:
        <br></br>
        <br></br>
        <Table dataSource={dataSource} columns={columns} pagination={{ pageSize: 5 }}/>
        Please note: in order to get your equation to render please put a $ at the beginning and end of the input

    </div>
  );
}
