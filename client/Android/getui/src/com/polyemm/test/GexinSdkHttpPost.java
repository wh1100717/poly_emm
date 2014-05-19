package com.polyemm.test;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLEncoder;
import java.util.Map;

import org.json.simple.JSONObject;

public class GexinSdkHttpPost {

	public static final String SERVICEURL = "http://10.0.2.2/android/pull";
	public static final int CONNECTION_TIMEOUT_INT = 8000;
	public static final int READ_TIMEOUT_INT = 5000;

	public static String httpPost(Map<String, Object> map) {
		String result="";
		String param = JSONObject.toJSONString(map);

		if (param != null) {

			URL url = null;

			try {
				url = new URL(SERVICEURL);
				HttpURLConnection urlConn = (HttpURLConnection) url.openConnection();
				urlConn.setDoInput(true); 
				urlConn.setDoOutput(true); 
				urlConn.setRequestMethod("POST");
				urlConn.setUseCaches(false); 
				urlConn.setRequestProperty("Charset", "utf-8");
				urlConn.setConnectTimeout(CONNECTION_TIMEOUT_INT);
				urlConn.setReadTimeout(READ_TIMEOUT_INT);

				urlConn.connect(); 

				DataOutputStream dop = new DataOutputStream(urlConn.getOutputStream());
				dop.write(param.getBytes("utf-8")); 
				
				dop.flush(); 
				dop.close(); 

				
				BufferedReader bufferReader = new BufferedReader(new InputStreamReader(urlConn.getInputStream()));
				String readLine = null;
				while ((readLine = bufferReader.readLine()) != null) {
					result += readLine;
				}
				bufferReader.close();
				urlConn.disconnect();
				System.out.println("result" + result);
				
			} catch (MalformedURLException e) {
				e.printStackTrace();
			} catch (IOException e) {
				e.printStackTrace();
			}
		} else {
			System.out.println("param is null");
			
		}
		return result;
	}

}
