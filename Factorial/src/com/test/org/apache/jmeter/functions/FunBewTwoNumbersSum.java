package com.test.org.apache.jmeter.functions;

import java.util.Collection;
import java.util.LinkedList;
import java.util.List;

import org.apache.jmeter.engine.util.CompoundVariable;
import org.apache.jmeter.functions.AbstractFunction;
import org.apache.jmeter.functions.InvalidVariableException;
import org.apache.jmeter.samplers.SampleResult;
import org.apache.jmeter.samplers.Sampler;
import org.apache.jmeter.threads.JMeterVariables;
import org.apache.jmeter.util.JMeterUtils;
import org.apache.jorphan.logging.LoggingManager;
import org.apache.log.Logger;

public class FunBewTwoNumbersSum extends AbstractFunction {
	@SuppressWarnings("unused")
	private static final Logger log = LoggingManager.getLoggerForClass();
	private static final List<String> desc = new LinkedList<String>();
	private static final String KEY = "__funBewTwoNumbersSum";
	private Object[] values = null;
	private CompoundVariable varName, minimum, maximum;
	static {
		desc.add("the min value of number");
		desc.add("the max value of number");
		desc.add(JMeterUtils.getResString("function_name_paropt"));
	}

	@Override
	public String execute(SampleResult previousResult, Sampler currentSampler)
			throws InvalidVariableException {
		long minNum, maxNum;
		String minnumberString = minimum.execute().trim();
		String maxnumberString = maximum.execute().trim();
		try {
			minNum = Long.valueOf(minnumberString).longValue();
			maxNum = Long.valueOf(maxnumberString).longValue();
		} catch (Exception e) {
			return null;
		}
		String sumString = String.valueOf(bewTwoNumbersSum(minNum, maxNum));
		if (varName != null) {
			JMeterVariables vars = getVariables();
			final String varTrim = varName.execute().trim();
			if (vars != null && varTrim.length() > 0) {
				vars.put(varTrim, sumString);
			}
		}

		return sumString;
	}

	private long bewTwoNumbersSum(long minnum, long maxnum)
			throws InvalidVariableException {
		long sum = 0;
		if (minnum < maxnum) {

			for (long i = minnum; i <= maxnum; i++) {
				sum += i;
			}
			return sum;
		}
		if (minnum == maxnum) {
			return maxnum + minnum;
		} else {
			throw new InvalidVariableException(
					"paramters not right,the min number must less than the max number!!!");
		}
	}

	@Override
	public void setParameters(Collection<CompoundVariable> parameters)
			throws InvalidVariableException {
		checkParameterCount(parameters, 2, 3);
		values = parameters.toArray();
		minimum = (CompoundVariable) values[0];
		maximum = (CompoundVariable) values[1];
		if (values.length > 2) {
			varName = (CompoundVariable) values[2];
		} else {
			varName = null;
		}
	}

	@Override
	public List<String> getArgumentDesc() {

		return desc;
	}

	@Override
	public String getReferenceKey() {

		return KEY;
	}

}
