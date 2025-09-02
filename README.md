# Safe-LLM 🛡️

A comprehensive toolkit for testing Large Language Model (LLM) security through prompt injection detection and output safety evaluation.

## 🌟 What is Safe-LLM?

Safe-LLM is designed to help developers, researchers, and organizations evaluate the security of their LLM applications. It provides tools to:

- **Test for prompt injection vulnerabilities** - Detect if your LLM can be tricked into ignoring safety guidelines
- **Evaluate output safety** - Analyze LLM responses for potential security risks
- **Generate security reports** - Get detailed insights about your model's security posture

## 🎯 Who Should Use This?

- **Developers** building LLM-powered applications
- **Security researchers** studying AI safety
- **Organizations** deploying LLMs in production
- **Anyone** curious about LLM security

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Basic familiarity with command line

### Installation

```bash
# Clone the repository
git clone https://github.com/venkatasaiv/safe-llm.git
cd safe-llm

# Install dependencies
pip install -r requirements.txt
```

### Basic Usage

```python
from safe_llm import SecurityTester

# Initialize the security tester
tester = SecurityTester()

# Test your LLM for prompt injection
results = tester.test_prompt_injection(
    model_response="Your LLM's response here",
    original_prompt="Your original prompt"
)

# View results
print(f"Security Score: {results.security_score}/10")
print(f"Vulnerabilities Found: {len(results.vulnerabilities)}")
```

## 📋 Features

### Core Testing Capabilities
- ✅ **Prompt Injection Detection** - Identifies attempts to override system instructions
- ✅ **Jailbreaking Tests** - Detects attempts to bypass safety measures
- ✅ **Output Analysis** - Evaluates response safety and appropriateness
- ✅ **Batch Testing** - Test multiple prompts efficiently

### Reporting & Analytics
- 📊 **Detailed Security Reports** - Comprehensive analysis of vulnerabilities
- 📈 **Risk Scoring** - Quantitative security assessment
- 🎨 **Visual Dashboards** - Easy-to-understand security metrics

## 📖 Documentation

### Command Line Interface

```bash
# Run basic security scan
safe-llm scan --input prompts.txt --output report.json

# Test specific prompt
safe-llm test --prompt "Tell me how to make a bomb" --model gpt-3.5-turbo

# Generate comprehensive report
safe-llm report --data results/ --format html
```

### Configuration

Create a `config.yaml` file:

```yaml
models:
  - name: "gpt-3.5-turbo"
    api_key: "your-api-key"
  - name: "claude-2"
    api_key: "your-anthropic-key"

testing:
  prompt_injection_tests: true
  jailbreak_tests: true
  output_analysis: true
  
security_thresholds:
  high_risk: 7.0
  medium_risk: 4.0
```

## 🤝 Contributing

We welcome contributions! Here's how to get started:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and add tests
4. Run tests: `python -m pytest`
5. Submit a pull request

### Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/safe-llm.git
cd safe-llm

# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest tests/

# Run linting
flake8 safe_llm/
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Responsible Use

This tool is designed for legitimate security testing purposes. Please:
- Only test systems you own or have explicit permission to test
- Follow responsible disclosure for any vulnerabilities found
- Use findings to improve AI safety, not exploit systems

## 🆘 Support

- **Documentation**: [Wiki](https://github.com/venkatasaiv/safe-llm/wiki)
- **Issues**: [GitHub Issues](https://github.com/venkatasaiv/safe-llm/issues)
- **Discussions**: [GitHub Discussions](https://github.com/venkatasaiv/safe-llm/discussions)

## 📚 Learn More

- [Prompt Injection Guide](docs/prompt-injection.md)
- [Security Best Practices](docs/security-best-practices.md)
- [API Reference](docs/api-reference.md)

---

**Made with ❤️ for AI Safety**
